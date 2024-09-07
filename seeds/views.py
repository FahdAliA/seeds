from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from seeds.models import Events, Startups, GovernBdy, About
from seeds.serializers import EventsSerializer, StartupSerializer ,GovernBdySerializer, AboutSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EventsView(APIView):
   
    def get(self, request, format=None):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GovernbdyView(APIView):
    
    def get(self, request, format=None):
        governbdy = GovernBdy.objects.all()
        serializer = GovernBdySerializer(governbdy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GovernBdySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutView(APIView):
   
    def get(self, request, format=None):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartupsView(APIView):
   
    def get(self, request, format=None):
        startups = Startups.objects.all()
        serializer = StartupSerializer(startups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StartupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)