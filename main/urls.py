from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('main/login/', LoginView.as_view(template_name='main/main_login.html'), name='login'),
    path('main/logout/', LogoutView.as_view(), name='logout'),


]