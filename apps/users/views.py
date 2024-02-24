from django.views import generic

from django.contrib.auth import get_user_model
from apps.users.forms import SignUpForm

User = get_user_model()


class SignUpView(generic.CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/'
    template_name = 'users/sign_up.html'
