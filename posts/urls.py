from django.urls import path 
from .views import main, new, create, show, update, delete

app_name = "posts" 
urlpatterns = [    
    path('new/', new, name="new"),    
    path('create/', create, name="create"), 
    path('', main, name="main"),
    path('show/<int:id>', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),  
    ]