from django.urls import path
from .views import *

# BASE URL => http://127.0.0.1:8000/pcn/

urlpatterns = [
    path('home/', home_view, name='home'),
    path('services/', services_view, name='services'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('about/', about_view, name='about'),
    path('team/', team_view, name='team'),
    path('contact/', contact_view, name='contact'),
]
