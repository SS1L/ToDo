from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('board/', views.boardsPage, name='board'),
    path('logout/', views.logoutUser, name='logout'),
    path('update_task/<str:index>/', views.updateTask, name='update_task'),
    path('deleteTask/<str:index>/', views.deleteTask, name='delete_task'),
]