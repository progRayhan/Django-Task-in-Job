from app_1.models import Person, Person2
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Person2
        fields = '__all__'