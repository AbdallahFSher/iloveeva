from django.urls import path
from . import views

urlpatterns = [
    path('', views.affirmation_view, name='affirmation'),
]