from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add', add, name='post'),
    path('delete/<uuid:id>', delete, name='post' ),
    path('update/<uuid:id>', update, name='post'),
    path('update/updaterecord/<uuid:id>', updaterecord, name='post')
]
