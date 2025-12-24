from django.urls import path
from . import views
urlpatterns = [
    path('', views.startpage, name='index'),
    path('/upload', views.uploadpage, name ='uploadpage')

]
