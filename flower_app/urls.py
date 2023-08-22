from django.urls import path
from flower_app import views

urlpatterns = [
    path('', views.index, name='main_page'),

]
