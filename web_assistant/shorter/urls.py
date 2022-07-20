from django.urls import path, include
from .views import shorter, to_source_url

urlpatterns = [
    path('', shorter, name='shorter'),
    path('<str:url_id>/', to_source_url, name='to_source_url')
]
