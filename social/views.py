from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "social/home.html"

class AboutView(TemplateView):
    template_name = "social/about.html"

class ContactView(TemplateView):
    template_name = "social/contact.html"    