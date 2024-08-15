from django.urls import path 
from . import views

urlpatterns = [
    path('', views.all_sky , name ='all_sky'),
    path('<int:sky_id>/', views.sky_detail , name ='sky_detail'),
]   