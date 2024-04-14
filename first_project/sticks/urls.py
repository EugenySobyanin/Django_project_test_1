from django.urls import path
from sticks import views


app_name = 'sticks'

urlpatterns = [
    path('', views.homepage, name='homepage')
]