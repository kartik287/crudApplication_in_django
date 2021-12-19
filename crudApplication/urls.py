from django.urls import path
from .views import *

# BASE URL => http://127.0.0.1:8000/crudapp/

urlpatterns = [
    path('register/', add_employee, name='register'),
    path('view/', view_employee),
    path('edit/<int:id>', edit_employee),
    path('delete/<int:id>', delete_employee),
    path('update/<int:id>', update_employee),
]
