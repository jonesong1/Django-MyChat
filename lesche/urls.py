from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .forms import LoginForm

app_name = 'lesche'

urlpatterns = [
    path('', include('conversation.urls')),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
