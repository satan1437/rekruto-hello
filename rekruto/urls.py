from django.urls import path
from .views import index

urlpatterns = [
	path('url_name/', index),
]
