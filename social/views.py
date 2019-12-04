from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from social.models import Profile
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import ListView,DetailView
from django.http.response import HttpResponseRedirect


class HomeView(TemplateView):
    template_name = "social/home.html"

class AboutView(TemplateView):
    template_name = "social/about.html"

class ContactView(TemplateView):
    template_name = "social/contact.html"   
     
@method_decorator(login_required,name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["name","age","phone","status","gender","description","pic"]