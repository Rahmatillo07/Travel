from django.urls import path
from .views import (all_tickets,category_by_ticket,detail,user_login,user_register,create_ticket,update_ticket,
                    delete_ticket)

urlpatterns = [
    path('',all_tickets,name='index'),
    path('category/<int:category_id>/',category_by_ticket,name='category'),
    path('detail/<int:ticket_id>/',detail,name='detail'),
    path('login/',user_login,name='login'),
    path('register/',user_register,name='register'),
    path('create/',create_ticket,name='create'),
    path('update/<int:pk>/',update_ticket,name='update'),
    path('update/<int:pk>/',delete_ticket,name='delete'),
]