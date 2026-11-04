from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserUpdateForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CustomUserUpdateForm
    template_name = 'dashboard/update_profile.html'
    success_url = reverse_lazy('dashboard')
    success_message = 'Your profile was updated successfully.'

    def get_object(self):
        return self.request.user