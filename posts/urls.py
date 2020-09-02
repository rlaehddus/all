from django.urls import path 
from .views import *

app_name = "posts" 
urlpatterns = [    
    path('new/', new, name="new"),    
    path('create/', create, name="create"), 
    path('', main, name="main"),
    path('show/<int:id>/', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"), 
    path('<int:post_id>/create_comment/', create_comment, name="create_comment"), 
    path('update_comment/<int:id>', update_comment, name="update_comment"),
    path('delete_comment/<int:id>', delete_comment, name="delete_comment"),    
    path('<int:post_id>/post_like', post_like, name="post_like"),
    path('like_list/', like_list, name="like_list"),
    
    ]