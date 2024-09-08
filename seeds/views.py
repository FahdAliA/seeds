from rest_framework import status
from seeds.models import Events, Startups, GovernBdy, About
from seeds.serializers import EventsSerializer, StartupSerializer ,GovernBdySerializer, AboutSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics


class EventsView(generics.ListCreateAPIView):

    serializer_class = EventsSerializer
    queryset = Events.objects.all()

class GovernbdyView(generics.ListCreateAPIView):

    serializer_class = GovernBdySerializer
    queryset = GovernBdy.objects.all()


class AboutView(generics.ListCreateAPIView):

    serializer_class =  AboutSerializer
    queryset = About.objects.all()

class StartupsView(generics.ListCreateAPIView):

    serializer_class = StartupSerializer
    queryset = Startups.objects.all()
