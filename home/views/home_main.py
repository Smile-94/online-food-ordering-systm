from django.shortcuts import render

# Generic Classes
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/index.html'

