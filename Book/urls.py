
from django.urls import path,include

from Book.views import say_hello

urlpatterns = [
    path('<str:first_name>/', say_hello)
]
