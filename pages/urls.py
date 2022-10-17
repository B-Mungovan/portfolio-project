from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('navbar/', views.navbar),
    path('my_cv/', views.my_cv, name='my_cv'),
]
