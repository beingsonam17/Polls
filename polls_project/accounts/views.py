from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView
from django.contrib.auth import login,logout



# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # not instantiating class so no parenthesis
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'