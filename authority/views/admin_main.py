

# Generic Classes
from django.views.generic import TemplateView



class AdminHomeView(TemplateView):
    template_name = 'authority/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Home" 
        return context
    