from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('delete',views.delete_data, name="deletedata"),
    path('update',views.update_data, name="updatedata"),
    

   
]