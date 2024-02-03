from django.urls import path
from . import views
from .views import UserAccountUpdateView


urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('user/update/', UserAccountUpdateView.as_view(), name='user-update'),
]
