from django.urls import path
from app import views

urlpatterns = [
    path('', views.cafe_tanitim, name='home'),
    path('', views.cafe_tanitim, name='cafe_tanitim'),
    path('api/lezzetler/', views.api_lezzetler, name='api_lezzetler'),
]