from django.urls import path
from items import views

app_name = 'items'
urlpatterns = [
    path('category01/', views.category01, name='category01'),
    path('category02/', views.category02, name='category02'),
    path('category03/', views.category03, name='category03'),
    path('category04/', views.category04, name='category04'),
    path('category05/', views.category05, name='category05'),
    path('category06/', views.category06, name='category06'),
    path('orderCreate/', views.orderCreate, name='orderCreate'),
]