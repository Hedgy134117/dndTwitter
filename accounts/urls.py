from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signupView, name="signup"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout")
]