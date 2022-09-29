from django.urls import path
from cooker.views import home

urlpatterns = [
    path('', home),
]