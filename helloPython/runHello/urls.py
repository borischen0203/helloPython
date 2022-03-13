from django.urls import path
from . import views

urlpatterns = [
    path('runHello',views.index)
]