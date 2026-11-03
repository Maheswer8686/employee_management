from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-success/', views.logout_success_view, name='logout_success'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('employee/add/', views.add_employee_view, name='add_employee'),
    path('employee/<int:pk>/', views.employee_profile_view, name='employee_profile'),
    path('employee/<int:pk>/edit/', views.edit_employee_view, name='edit_employee'),
    path('employee/<int:pk>/delete/', views.delete_employee_view, name='delete_employee'),
    path('change-password/', views.change_password_view, name='change_password'),
]
