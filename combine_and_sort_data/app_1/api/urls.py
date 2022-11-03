from django.urls import path
from .views import person_and_person2,person, person2

urlpatterns = [
    path('', person_and_person2),
    path('person/', person),
    path('person2/', person2),
]