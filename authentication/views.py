from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .forms import UserCreateForm

class SignUpCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
