from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeLogin, name='homeLogin')

]