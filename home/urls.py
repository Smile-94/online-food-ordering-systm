from django.urls import path

# Views
from home.views import home_main

app_name = 'home'

urlpatterns = [

    path('', home_main.IndexView.as_view(),name="index"),
    path('home/', home_main.IndexView.as_view(),name="home"),
]