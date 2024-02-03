from django.urls import path
# from rest_framework.routers import DefaultRouter
# from . import views
from .views import EntryListCreateView, EntryRetrieveUpdateDestroyView, echo_text, GetEntriesFromVector


urlpatterns = [
    path('entries/', EntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<str:pk>/', EntryRetrieveUpdateDestroyView.as_view(), name='entry-retrieve-update-destroy'),
    path('echo/', echo_text, name='echo-text'),
    path('vector/', GetEntriesFromVector, name='get-entries-from-vector'),
]