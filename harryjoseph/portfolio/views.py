from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    """
    Home view that displays the portfolio page with work experince.
    We're using a simple list of dictionaries to store the job history
    since we don't need a database for this basic portfolio.
    """
    # print("Loading home page...")  # debugging - remove later
    
    # Work experence data - someone nearing retirement
    work_experience = [
        {
            'company': 'ABC Corporation', 
            'title': 'Senior Analyst',
            'start_date': '2010',
            'end_date': '2018'
        },
        {
            'company': 'XYZ Industries',
            'title': 'Project Manager', 
            'start_date': '2005',
            'end_date': '2010'
        },
        {
            'company': 'Technology Solutions Inc',
            'title': 'Team Lead',
            'start_date': '2000', 
            'end_date': '2005'
        }
    ]
    
    # Send this data to the template
    context = {
        'work_experience': work_experience  # TODO: maybe add more details later?
    }
    
    return render(request, 'portfolio/home.html', context)


def contact(request):
    """
    Contact view handles both GET and POST requests for the contact form.
    If it's a POST request with valid data, we'll redirect to thank you page.
    Otherwise, just display the contact form (with any validation errors).
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Store form data in session for the thank you page
            # Note: this could probably be done better with a model, but keeping it simple
            request.session['contact_name'] = form.cleaned_data['name']
            request.session['contact_phone'] = form.cleaned_data['phone'] 
            request.session['contact_message'] = form.cleaned_data['message']
            
            # Redirect to thank you page after successful form submission
            return redirect('thank_you')
    else:
        # Create empty form for GET request
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form})


def thank_you(request):
    """
    Thank you page displays the submitted contact information.
    Gets data from session that was stored during form submission.
    """
    # Get the contact info from session data
    contact_data = {
        'name': request.session.get('contact_name', 'Unknown'),
        'phone': request.session.get('contact_phone', 'Not provided'),
        'message': request.session.get('contact_message', 'No message')
    }
    
    # Clear the session data after displaying (optional cleanup)
    request.session.pop('contact_name', None)
    request.session.pop('contact_phone', None)
    request.session.pop('contact_message', None)
    
    return render(request, 'portfolio/thank_you.html', {'contact_data': contact_data})