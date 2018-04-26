from django.urls import path
from .views import index, Herocontent

urlpatterns = [
    path('', index),
    path('hero/<int:hero_id>', Herocontent)
]