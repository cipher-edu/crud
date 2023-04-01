from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add', add, name='add'),
    path('delete/<uuid:id>', delete, name='delete' ),
    path('edit/<uuid:id>', edit, name='edit')
    ]