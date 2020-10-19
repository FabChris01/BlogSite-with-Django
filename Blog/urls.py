from django.urls import path
from . import views

urlpatterns = [
    path("",views.landing, name="landing"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("TAC/", views.TAC, name="TAC"),
    path("selection/",views.selection, name="selection"),
    path("main/",views.main, name="main"),
]
