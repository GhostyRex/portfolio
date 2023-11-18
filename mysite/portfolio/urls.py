from django.urls import path
from .views import index, projects


urlpatterns = [
    path('', index, name='index'),
    path('projects/', projects, name='projects'),
]
