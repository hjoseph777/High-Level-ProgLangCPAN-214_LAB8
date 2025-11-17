from django.urls import path
from . import views

# URL patterns for the portfolio app
# Pretty straightforward routing here
urlpatterns = [
    path('', views.home, name='home'),  # Landing page
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),  # success page
]