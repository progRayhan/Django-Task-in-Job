from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()

    def __str__(self):
        return self.name


class Person2(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()

    def __str__(self):
        return self.name