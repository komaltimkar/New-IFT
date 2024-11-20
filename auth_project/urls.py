from django.contrib import admin
from django.urls import path
from auth_aapp import views  # Make sure to import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Add a path for the root URL (this will handle /)
    path('', views.login_view, name='home'),  # Or you can redirect to login, dashboard, or home page
]
