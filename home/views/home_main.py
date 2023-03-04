from django.shortcuts import render

# Generic Classes
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        return context

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Contact With Us'
        return context
    
    

