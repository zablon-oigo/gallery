from django.urls import path
from .views import home,photo_detail, delete_photo,create_photo,update_photo,search_photo

urlpatterns=[
    path('',home, name='home'),
    path('create/',create_photo, name='create'),
    path('<int:id>/',photo_detail, name='detail'),
    path('delete/<str:id>/',delete_photo, name='delete'),
    path('update/<int:id>/',update_photo, name='update'),
    path('search/', search_photo, name='search'),
]