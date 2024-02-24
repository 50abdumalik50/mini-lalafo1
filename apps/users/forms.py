from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'display_name',
            'avatar',
            'phone_number',
            'region',
        ]