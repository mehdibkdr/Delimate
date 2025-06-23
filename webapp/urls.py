from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD Record
    path('dashboard', views.dashboard, name="dashboard"),
    path('ongoing', views.ongoing, name='ongoing'),
    path('completed', views.completed, name='completed'),
    path('create-record', views.create_record, name="create-record"),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('record/<int:pk>', views.singular_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    
    # CRUD Deliverer
    path('deliverers/', views.deliverers_dashboard, name='deliverers_dashboard'),
    path('deliverers/create/', views.create_deliverer, name='create_deliverer'),
    path('deliverers/<int:pk>/update/', views.update_deliverer, name='update_deliverer'),
    path('deliverers/<int:pk>/view/', views.view_deliverer, name='view_deliverer'),
    path('deliverers/<int:pk>/delete/', views.delete_deliverer, name='delete_deliverer'),
    
]
