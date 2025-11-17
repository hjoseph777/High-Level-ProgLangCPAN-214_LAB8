from django import forms
import re

class ContactForm(forms.Form):
    """
    Contact form with validation for name, email, phone, and message fields.
    All fields are required and we'll validate the email and phone number formats.
    Pretty straightforward stuff here.
    """
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your full name',
        }),
        help_text='Please enter your full name'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your email address',
        }),
        help_text='Please enter a valid email address'
    )
    
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your phone number',
        }),
        help_text='Phone number in any common format'
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Enter your message here...',
            'rows': 5,
        }),
        help_text='Please enter your message or inquiry'
    )
    
    def clean_phone(self):
        """
        Custom validation for phone number field.
        Accepts various formats but ensures it contains digits.
        Not perfect but it works for our needs.
        """
        phone = self.cleaned_data.get('phone')
        
        # Remove all non-digit characters to check basic format
        digits_only = re.sub(r'\D', '', phone)
        # print(f"Cleaned phone: {digits_only}")  # debug
        
        # Check if we have at least 10 digits (US phone number standard)
        if len(digits_only) < 10:
            raise forms.ValidationError('Phone number must contain at least 10 digits.')
        
        # Check if it's not too long (max 15 digits for international)
        if len(digits_only) > 15:
            raise forms.ValidationError('Phone number cannot exceed 15 digits.')
        
        return phone  # Return the original formatted version
    
    def clean_name(self):
        """
        Validation for name field - make sure it's not just spaces
        and contains at least some letters.
        """
        name = self.cleaned_data.get('name')
        
        if not name or name.strip() == '':
            raise forms.ValidationError('Name cannot be empty.')
        
        # Check if name contains at least some letters
        if not re.search(r'[a-zA-Z]', name):
            raise forms.ValidationError('Name must contain at least some letters.')
        
        return name.strip()  # Remove extra whitespace