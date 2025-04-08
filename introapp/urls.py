from django.urls import path
from .views import create_user, user_created, success, user_list

app_name = 'introapp'

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('user_created/<int:user_id>/', user_created, name='user_created'),
    path('success/', success, name='success'),
    path('user_list/', user_list, name='user_list'),
]
