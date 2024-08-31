from django.urls import path
from seeds import views

urlpatterns = [
    path("events",views.EventsView,name="Events"),
    path("startups",views.StartupsView,name="Startups"),
    path("governbdy",views.GovernbdyView,name="Governing_Body"),
    path("",views.AboutView,name="about"),

]