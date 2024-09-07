from rest_framework import serializers
from seeds.models import Events, Startups, GovernBdy, About

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startups
        fields = '__all__'
    def create(self, validated_data):
        return super().create(validated_data)

class GovernBdySerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernBdy
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About
        fields = '__all__'