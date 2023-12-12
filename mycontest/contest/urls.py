# contest/urls.py
from django.urls import path
from .views import contest_entry

urlpatterns = [
    path('entry/', contest_entry, name='contest_entry'),
]
