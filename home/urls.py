from django.urls import path

# Views
from home.views import home_main
from home.views import customer_message

app_name = 'home'

urlpatterns = [

    path('', home_main.IndexView.as_view(),name="index"),
    path('home/', home_main.IndexView.as_view(),name="home"),
    path('contact/', home_main.ContactView.as_view(),name="contact"),
    
]

urlpatterns += [
    path('customer-message/', customer_message.CustomerMessageView.as_view(), name='customer_message'),
]
