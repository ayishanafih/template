from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Name the URL for index view
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
