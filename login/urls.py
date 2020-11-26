from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth
from .forms import LoginForm
from django.contrib import admin

urlpatterns = [
    path('', views.blank),
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.blank),
    path('accounts/login/',LoginView.as_view(
            template_name='login.html',
            authentication_form=LoginForm
        )
    ),
    # path('login/', LoginView.as_view(
    #         template_name='login.html',
    #         authentication_form=LoginForm
    #     )
    # ),
    path('accounts/logout/', auth.logout_then_login),
    path('accounts/register/',views.register),
    path('accounts/password_reset/done/', auth.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("accounts/password_reset", views.password_reset_request, name="password_reset")
]