from django.urls import path

app_name = 'authority'

# Views
from authority.views import admin_main

urlpatterns = [
    path('authority/', admin_main.AdminHomeView.as_view(), name='authority')
    
]