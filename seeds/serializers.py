from rest_framework import serializers
from seeds.models import Events, Startups, GovernBdy, About

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['title','description','img','date',]


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startups
        fields = ['name','year','owner','description',]

class GovernBdySerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernBdy
        fields = ['name','position','photo',]

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About
        field=['mission','vision','objectives',]