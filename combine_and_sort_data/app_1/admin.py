from django.contrib import admin
from app_1.models import Person, Person2

class AdminPerson(admin.ModelAdmin):
    list_display = ('name', 'created')

class AdminPerson2(admin.ModelAdmin):
    list_display = ('name', 'created')

# Register your models here.
admin.site.register(Person, AdminPerson)
admin.site.register(Person2, AdminPerson2)