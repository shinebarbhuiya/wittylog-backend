from django.urls import path
# from rest_framework.routers import DefaultRouter
# from . import views
from .views import EntryListCreateView, EntryRetrieveUpdateDestroyView


urlpatterns = [
    # path('entries/', views.EntryList.as_view(), name='entry-list'),
    # path('entries/<int:pk>/', views.EntryDetail.as_view(), name='entry-detail'),
    path('entries/', EntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<str:pk>/', EntryRetrieveUpdateDestroyView.as_view(), name='entry-retrieve-update-destroy'),
]