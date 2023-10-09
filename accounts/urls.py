from django.urls import path 
from .views import *

app_name='accounts'

app_name='users'
urlpatterns=[
    path('login/',sign_in, name='login'),
    path('logout/',sign_out, name='logout'),
    path('reg/',sign_up, name='register'),
]