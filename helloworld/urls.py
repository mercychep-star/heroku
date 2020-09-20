from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloView, name='helo'),
    path('users', views.anotherView, name='view2')
]