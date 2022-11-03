from rest_framework.decorators import api_view
from app_1.models import Person, Person2
from rest_framework.response import Response
from app_1.api.serializers import PersonSerializer, PersonSerializer2
from rest_framework.views import APIView
from operator import itemgetter


@api_view(['GET'])
def person_and_person2(request):
    if request.method == 'GET':
        person = Person.objects.all()[:5]
        person2 = Person2.objects.all()[:5]
        personSerializer = PersonSerializer(person, many=True)
        person2Serializer = PersonSerializer2(person2, many=True)
        data = personSerializer.data+person2Serializer.data
        a = sorted(data, key=itemgetter('created'))
        print(data)

        return Response(a)

@api_view(['GET','POST'])
def person(request):
    if request.method == 'GET':
        person  = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','POST'])
def person2(request):
    if request.method == 'GET':
        person  = Person2.objects.all()
        serializer = PersonSerializer2(person, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PersonSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

