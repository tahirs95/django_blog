from django.contrib import admin
from django.urls import path, include
from .views import display_view,create_view,detail_view


urlpatterns = [
    path('', display_view, name='display_view'),
    path('add', create_view, name='create_view'),
    path('<id>', detail_view, name='detail_view' ),

]