from django.urls import path
from . import views

urlpatterns = [
    path('ai',views.Ai,name='ai')
]