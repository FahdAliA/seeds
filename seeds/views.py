from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from seeds.models import Events, Startups, GovernBdy
from seeds.serializers import EventsSerializer, StartupSerializer ,GovernBdySerializer



@api_view(['GET',])
def EventsView(request):
    queryset = Events.objects.all()
    serializer = EventsSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def StartupsView(request):
    queryset = Startups.objects.all()
    serializer = StartupSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def GovernbdyView(request):
    queryset = GovernBdy.objects.all()
    serializer = GovernBdySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def AboutView(request):
    queryset = About.objects.all()
    serializer = AboutSerializer(queryset)
    return Response(serializer.data)