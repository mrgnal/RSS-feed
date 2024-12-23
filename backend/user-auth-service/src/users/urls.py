from django.urls import path, include
from .views import LoginView, RegisterView, GoogleAuthInitView, GoogleAuthCallbackView, change_password, \
    UserProfileUpdateView, UserProfileDeleteView, SendEmailView, CustomTokenVerifyView, RefreshView
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('google/login/', GoogleAuthInitView.as_view(), name='google_auth_init'),
    path('google/login/callback/', GoogleAuthCallbackView.as_view(), name='google_auth_callback'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('change_account_data/', UserProfileUpdateView.as_view(), name='change_data'),
    path('delete_profile/', UserProfileDeleteView.as_view(), name='delete_profile'),
    path('send_email/', SendEmailView.as_view(), name='send_email'),
    path('verify_token/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('jwt/refresh', RefreshView.as_view(), name='token_refresh'),
]
