from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('home/', views.home_view, name='home'),  # Home page
    path('profile/', views.profile_view, name='profile'),  # Profile page
    path('search/', views.search_view, name='search'),  # Search page
    path('messages/', views.messages_view, name='messages'),  # Messages page
    path('notifications/', views.notifications_view, name='notifications'),  # Notifications page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Registration page
]
