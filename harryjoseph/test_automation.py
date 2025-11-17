"""
Automated Testing Script for Harry Joseph Portfolio Django Application
======================================================================

This script performs automated testing of the Django web application
following the required testing scenarios:
1. Start Django server (manual step)
2. Test home webpage access
3. Test contact webpage access
4. Test partial form submission (validation errors)
5. Test complete form submission (success flow)

Run this script with: python test_automation.py
"""

import requests
import sys
import time
from urllib.parse import urljoin

class DjangoPortfolioTester:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.results = []
        
    def log_result(self, test_name, status, details):
        """Log test results"""
        result = {
            'test': test_name,
            'status': status,
            'details': details,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        self.results.append(result)
        print(f"✅ {test_name}: {status}" if status == "PASS" else f"❌ {test_name}: {status}")
        print(f"   Details: {details}\n")
        
    def test_server_running(self):
        """Test Scenario 1: Check if Django server is running"""
        try:
            response = self.session.get(self.base_url, timeout=5)
            if response.status_code == 200:
                self.log_result(
                    "Django Server Running", 
                    "PASS", 
                    f"Server responding at {self.base_url}"
                )
                return True
            else:
                self.log_result(
                    "Django Server Running", 
                    "FAIL", 
                    f"Server returned status code: {response.status_code}"
                )
                return False
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Django Server Running", 
                "FAIL", 
                f"Cannot connect to server: {str(e)}"
            )
            return False
            
    def test_home_page(self):
        """Test Scenario 2: Navigate to home webpage"""
        try:
            response = self.session.get(self.base_url)
            if response.status_code == 200 and "Harry Joseph" in response.text:
                self.log_result(
                    "Home Page Access", 
                    "PASS", 
                    f"Status: {response.status_code}, Contains portfolio content"
                )
                return True
            else:
                self.log_result(
                    "Home Page Access", 
                    "FAIL", 
                    f"Status: {response.status_code}, Missing expected content"
                )
                return False
        except Exception as e:
            self.log_result("Home Page Access", "FAIL", f"Error: {str(e)}")
            return False
            
    def test_contact_page(self):
        """Test Scenario 3: Navigate to contact webpage"""
        try:
            contact_url = urljoin(self.base_url, '/contact/')
            response = self.session.get(contact_url)
            
            if response.status_code == 200:
                # Check for form elements more specifically - Django form patterns
                has_form = '<form' in response.text
                has_csrf = 'csrfmiddlewaretoken' in response.text
                # Check for Django form field patterns (id_fieldname is Django default)
                has_name = 'id_name' in response.text or 'name="name"' in response.text
                has_email = 'id_email' in response.text or 'name="email"' in response.text  
                has_phone = 'id_phone' in response.text or 'name="phone"' in response.text
                has_message = 'id_message' in response.text or 'name="message"' in response.text
                
                if has_form and has_csrf and has_name and has_email and has_phone and has_message:
                    self.log_result(
                        "Contact Page Access", 
                        "PASS", 
                        f"Status: {response.status_code}, Form with CSRF and required fields present"
                    )
                    return True
                else:
                    self.log_result(
                        "Contact Page Access", 
                        "PARTIAL", 
                        f"Status: {response.status_code}, Missing form elements"
                    )
                    return False
            else:
                self.log_result(
                    "Contact Page Access", 
                    "FAIL", 
                    f"Status: {response.status_code}"
                )
                return False
        except Exception as e:
            self.log_result("Contact Page Access", "FAIL", f"Error: {str(e)}")
            return False
            
    def get_csrf_token(self, response_text):
        """Extract CSRF token from response"""
        import re
        csrf_pattern = r'<input[^>]*name=["\']csrfmiddlewaretoken["\'][^>]*value=["\']([^"\']*)["\']'
        match = re.search(csrf_pattern, response_text)
        return match.group(1) if match else None
        
    def test_partial_form_submission(self):
        """Test Scenario 4: Partial form submission to generate validation errors"""
        try:
            # First get the contact page to retrieve CSRF token
            contact_url = urljoin(self.base_url, '/contact/')
            get_response = self.session.get(contact_url)
            csrf_token = self.get_csrf_token(get_response.text)
            
            if not csrf_token:
                self.log_result(
                    "Partial Form Submission", 
                    "FAIL", 
                    "Could not retrieve CSRF token"
                )
                return False
                
            # Submit partial form data (invalid)
            form_data = {
                'csrfmiddlewaretoken': csrf_token,
                'name': 'John',  # Valid
                'email': 'invalid-email',  # Invalid format
                'phone': '123',  # Too short
                'message': ''  # Empty (required)
            }
            
            response = self.session.post(contact_url, data=form_data)
            
            # Should return to contact page with errors (status 200)
            if response.status_code == 200:
                # Check for error indicators
                has_errors = any(error_text in response.text.lower() for error_text in 
                               ['error', 'invalid', 'required', 'enter a valid'])
                
                if has_errors:
                    self.log_result(
                        "Partial Form Submission", 
                        "PASS", 
                        "Form validation errors displayed correctly"
                    )
                    return True
                else:
                    self.log_result(
                        "Partial Form Submission", 
                        "PARTIAL", 
                        "Form submitted but validation errors not clearly visible"
                    )
                    return False
            else:
                self.log_result(
                    "Partial Form Submission", 
                    "FAIL", 
                    f"Unexpected status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_result("Partial Form Submission", "FAIL", f"Error: {str(e)}")
            return False
            
    def test_complete_form_submission(self):
        """Test Scenario 5: Complete form submission to reach thank_you page"""
        try:
            # Get CSRF token
            contact_url = urljoin(self.base_url, '/contact/')
            get_response = self.session.get(contact_url)
            csrf_token = self.get_csrf_token(get_response.text)
            
            if not csrf_token:
                self.log_result(
                    "Complete Form Submission", 
                    "FAIL", 
                    "Could not retrieve CSRF token"
                )
                return False
                
            # Submit complete valid form data
            form_data = {
                'csrfmiddlewaretoken': csrf_token,
                'name': 'John Smith',
                'email': 'john.smith@example.com',
                'phone': '1234567890',
                'message': 'This is a test message for the automated testing.'
            }
            
            response = self.session.post(contact_url, data=form_data)
            
            # Should redirect to thank you page (status 302) or directly show thank you (200)
            if response.status_code in [200, 302]:
                # Check if we're on thank you page or redirected
                final_url = response.url if hasattr(response, 'url') else contact_url
                
                # If redirected, follow the redirect
                if response.status_code == 302:
                    thank_you_response = self.session.get(response.headers.get('Location', '/thank_you/'))
                    content = thank_you_response.text
                else:
                    content = response.text
                    
                # Check for thank you page indicators
                success_indicators = ['thank you', 'success', 'submitted', 'John Smith']
                has_success = any(indicator.lower() in content.lower() for indicator in success_indicators)
                
                if has_success:
                    self.log_result(
                        "Complete Form Submission", 
                        "PASS", 
                        "Form submitted successfully, thank you page displayed"
                    )
                    return True
                else:
                    self.log_result(
                        "Complete Form Submission", 
                        "PARTIAL", 
                        "Form submitted but success confirmation unclear"
                    )
                    return False
            else:
                self.log_result(
                    "Complete Form Submission", 
                    "FAIL", 
                    f"Unexpected status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_result("Complete Form Submission", "FAIL", f"Error: {str(e)}")
            return False
            
    def run_all_tests(self):
        """Execute all test scenarios"""
        print("🧪 STARTING AUTOMATED TESTING - Harry Joseph Portfolio")
        print("=" * 60)
        print()
        
        # Check if server is running first
        server_running = self.test_server_running()
        if not server_running:
            print("❌ Cannot proceed - Django server not running!")
            print("Please start the server with: python manage.py runserver")
            return False
            
        # Run all test scenarios
        tests = [
            self.test_home_page,
            self.test_contact_page,
            self.test_partial_form_submission,
            self.test_complete_form_submission
        ]
        
        passed = 1 if server_running else 0  # Count the server test
        total_tests = len(tests) + 1  # Include server test in total
        
        for test in tests:
            if test():
                passed += 1
                
        print("=" * 60)
        print(f"🏁 TESTING COMPLETE: {passed}/{total_tests} tests passed")
        
        return passed == total_tests
        
    def generate_report(self):
        """Generate a formatted test report"""
        report = "# AUTOMATED TEST RESULTS\n\n"
        report += f"**Test Run Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        for result in self.results:
            status_emoji = "✅" if result['status'] == "PASS" else "❌" if result['status'] == "FAIL" else "⚠️"
            report += f"{status_emoji} **{result['test']}:** {result['status']}\n"
            report += f"   - Details: {result['details']}\n\n"
            
        return report

def main():
    """Main execution function"""
    print("Automated Testing Script for Harry Joseph Portfolio")
    print("Please ensure the Django development server is running at http://127.0.0.1:8000")
    print()
    
    tester = DjangoPortfolioTester()
    success = tester.run_all_tests()
    
    # Generate and save report
    report = tester.generate_report()
    with open('test_results.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n📄 Test report saved to: test_results.md")
    
    if success:
        print("🎉 All tests passed successfully!")
        return 0
    else:
        print("⚠️  Some tests failed. Check the report for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())