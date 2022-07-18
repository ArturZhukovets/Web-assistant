from django.urls import path, include
from .views import shorter

urlpatterns = [
    path('', shorter, name='shorter')
]
