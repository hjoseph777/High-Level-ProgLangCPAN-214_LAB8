## Harry Joseph Portfolio - Django Web Application

## Project Metadata
- Author: High-Level Programming Languages CPAN 214
- Created: November 17, 2025
- Platform: Django Web Framework (Python)
- Package Manager: pip
- Framework: Django 5.2.8
- Database: SQLite (default)
- Routing: URL-based routing

## Overview
Harry Joseph Portfolio is a comprehensive Django web application showcasing professional portfolio information with interactive contact functionality. The project demonstrates Django best practices including template inheritance, form handling, validation, and responsive design.

## Quick Download

**Get the complete project instantly:**

 ![Download High-Level-ProgLangCPAN-214_LAB8](https://img.shields.io/badge/Download-High--Level--ProgLangCPAN--214__LAB8.zip-blue?style=for-the-badge&logo=download)

[![Download High-Level-ProgLangCPAN-214_LAB8](https://img.shields.io/badge/Download-High--Level--ProgLangCPAN--214__LAB8.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/High-Level-ProgLangCPAN-214_LAB8/releases/download/v1.0/High-Level-ProgLangCPAN-214_LAB8.zip)

 [![Download HarryJosephPortfolio](https://img.shields.io/badge/Download-HarryJosephPortfolio.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/HarryJosephPortfolio/releases/download/v1.0/HarryJosephPortfolio.zip)

[![Download Lab8Portfolio](https://img.shields.io/badge/Download-Lab8Portfolio.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/Lab8Portfolio/releases/download/v1.0/Lab8Portfolio.zip)


[![Download Lab8](https://img.shields.io/badge/Download-Lab8Portfolio.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/High-LevelProgLangCPAN214_LAB8/releases/download/v1.0/High-LevelProgLangCPAN214_LAB8.zip)


[![Download HarryJosephPortfolio](https://img.shields.io/badge/Download-High-LevelProgLangCPAN214_LAB8.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/High-LevelProgLangCPAN214_LAB8/releases/download/v1.0/High-LevelProgLangCPAN214_LAB8.zip)

*Complete Django project with portfolio display and contact form ready to run*

## Live Demo

**Experience the portfolio in action:**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-View%20Portfolio-green?style=for-the-badge&logo=django)](http://127.0.0.1:8000/)

*Interactive Django web application - Start the development server to view*

## Application Demo & Screenshots

### Visual Application Walkthrough

Experience the Harry Joseph Portfolio through these comprehensive screenshots showcasing all key features and functionality:

#### 1. **Portfolio Home Page**
<div align="center">
<img src="harryjoseph/static/images/mainScreenshot.png" alt="Harry Joseph Portfolio - Home Page" width="800px">
<br><i>Professional portfolio homepage displaying work experience and navigation</i>
</div>

---

#### 2. **Contact Form Interface**
<div align="center">
<img src="harryjoseph/static/images/contactmainScreenshotF.png" alt="Contact Form - User Interface" width="800px">
<br><i>Interactive contact form with validation and professional styling</i>
</div>

---

#### 3. **Form Validation in Action** 
<div align="center">
<img src="harryjoseph/static/images/messagemainScreenshotS.png" alt="Form Validation - Error Display" width="800px">
<br><i>Real-time form validation showing error messages and user feedback</i>
</div>

---

#### 4. **Successful Form Submission**
<div align="center">
<img src="harryjoseph/static/images/contactmainScreenshotSuccess.png" alt="Thank You Page - Success" width="800px">
<br><i>Thank you page displaying submitted contact information confirmation</i>
</div>

---

#### 5. **Automated Testing Results**
<div align="center">
<img src="harryjoseph/static/images/ScreenshotAuatomatedtest.png" alt="Automated Testing - 5/5 Tests Passed" width="800px">
<br><i>Complete automated testing suite showing all 5 tests passing successfully</i>
</div>

### Key Features Demonstrated
- **Professional Portfolio Layout** - Clean, responsive design
- **Secure Form Handling** - CSRF protection and validation
- **Real-time Validation** - Instant feedback for user inputs
- **User Experience** - Smooth navigation and feedback
- **Quality Assurance** - Comprehensive automated testing

## Important: Where your main Django code lives
- The main views logic is in [`harryjoseph/portfolio/views.py`](harryjoseph/portfolio/views.py) with home, contact, and thank you views
- The Django forms are in [`harryjoseph/portfolio/forms.py`](harryjoseph/portfolio/forms.py) with contact form validation
- Templates are in [`harryjoseph/portfolio/templates/portfolio/`](harryjoseph/portfolio/templates/portfolio/) with base, home, contact, and thank you templates

## Project Explorer
An interactive, collapsible view of the Django codebase. Click file names to open them.

<details open>
   <summary><strong>harryjoseph/ – Main Project Directory</strong></summary>

   - **harryjoseph**
      - [`__init__.py`](harryjoseph/harryjoseph/__init__.py) – Package marker
      - [`settings.py`](harryjoseph/harryjoseph/settings.py) – **Django configuration & settings**
      - [`urls.py`](harryjoseph/harryjoseph/urls.py) – **Main URL routing**
      - [`wsgi.py`](harryjoseph/harryjoseph/wsgi.py) – WSGI application entry point
      - [`asgi.py`](harryjoseph/harryjoseph/asgi.py) – ASGI application entry point
</details>

<details>
   <summary><strong>portfolio/ – Portfolio Django App</strong></summary>

   - **portfolio**
      - [`__init__.py`](harryjoseph/portfolio/__init__.py) – Package marker
      - [`views.py`](harryjoseph/portfolio/views.py) – **Main view functions (home, contact, thank you)**
      - [`forms.py`](harryjoseph/portfolio/forms.py) – **Django forms with validation**
      - [`urls.py`](harryjoseph/portfolio/urls.py) – **App-specific URL routing**
      - [`apps.py`](harryjoseph/portfolio/apps.py) – App configuration
      - [`admin.py`](harryjoseph/portfolio/admin.py) – Admin interface config
      - [`models.py`](harryjoseph/portfolio/models.py) – Database models (empty)
      - [`tests.py`](harryjoseph/portfolio/tests.py) – Test cases
      - **templates/portfolio/**
         - [`base.html`](harryjoseph/portfolio/templates/portfolio/base.html) – **Base template with navigation**
         - [`home.html`](harryjoseph/portfolio/templates/portfolio/home.html) – **Portfolio/home page**
         - [`contact.html`](harryjoseph/portfolio/templates/portfolio/contact.html) – **Contact form page**
         - [`thank_you.html`](harryjoseph/portfolio/templates/portfolio/thank_you.html) – **Form success page**
</details>

<details>
   <summary><strong>Database & Management</strong></summary>

   - [`db.sqlite3`](harryjoseph/db.sqlite3) – SQLite database (auto-generated)
   - [`manage.py`](harryjoseph/manage.py) – **Django management script**
   - [`README.md`](README.md) – Documentation (this file)
</details>



*This project demonstrates modern Django web development techniques with proper form handling, validation, and template inheritance.*
