from django.urls import path

from apps.users.views import SignUpView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up')
]