from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register', views.registration, name = 'register'),
    path('login', views.UserLoginView.as_view(), name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('update-profile', views.update_profile, name ='update-profile'), 

    # password reset urls
   path('reset_password', auth_views.PasswordResetView.as_view(template_name = 'users/password-reset.html'), name='password-reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'), name = 'password_reset_done'),
    
    
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-form.html'), name = 'password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'), name = 'password_reset_complete'),
    
    
    
  
]
