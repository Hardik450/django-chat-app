# chat/urls.py
from django.urls import path
from .views import signup_view, chat_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
