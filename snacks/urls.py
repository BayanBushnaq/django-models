from django.urls import path
from .views import HomePage , SnacksListView , SnackDetails
urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('snacks/',SnacksListView.as_view(),name='snacks'),
    path('snacks/<pk>',SnackDetails.as_view(),name='details')
]