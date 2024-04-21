from django.urls import path
from .views import fruitview

urlpatterns=[
    path('fview/',fruitview)
]