from django.urls import path
from app_1.api.views import ProductView

urlpatterns = [
    path('',ProductView.as_view()),
]