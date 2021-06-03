from django.urls import path
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('accounts/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', PasswordResetConfirmView.as_view, name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]