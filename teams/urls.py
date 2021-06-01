from django.urls import path

from .views import add

app_name = 'teams'

urlpatterns = [
    path('add/', add, name='add'),
]