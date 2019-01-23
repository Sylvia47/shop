from django.urls import path
from signin import views


app_name = 'signin'
urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
