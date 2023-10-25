from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('bidule', views.bidule, name='home_bidule'),
    path('messages', views.all_messages, name='all_messages'),
    path('messages/new_message', views.new_message, name='new_message'),
    path('messages/modify/<str:id>', views.edit_message, name='edit_message'),
    path('messages/delete/<str:id>', views.delete_message, name='delete_message'),
    path('messages/response/add/<str:id>', views.add_response, name='response_message'),
    path('messages/response/delete/<str:id>', views.delete_response, name='delete_response'),
    path('messages/response/modify/<str:id>', views.edit_response, name='edit_response'),
    path('messages/show/<str:id>', views.show_message, name='show_message'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

]
