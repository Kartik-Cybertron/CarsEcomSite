from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registrationPage,name="register"),
]
