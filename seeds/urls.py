from django.urls import path
from seeds import views

urlpatterns = [
    path("events",views.EventsView.as_view(),name="Events"),
    path("startups",views.StartupsView.as_view(),name="Startups"),
    path("governbdy",views.GovernbdyView.as_view(),name="Governing_Body"),
    path("",views.AboutView.as_view(),name="about"),

]