from django.urls import path
from . import views  # Import views from the current app
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #==========================================================
    path('home/', views.home_view, name='home'),  # Home page
    #=============================================================
    path('profile/', views.profile_view, name='profile'),

    path('gallery/', views.gallery_view, name='gallery'),  # Ensure a trailing slash for consistency
    path('add/', views.add_post_view, name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post_view, name='edit_post'),  # New edit URL
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
    #==================================================================
    path('search/', views.search_view, name='search'),  # Search page
    path('messages/', views.messages_view, name='messages'),  # Messages page
    path('notifications/', views.notifications_view, name='notifications'),  # Notifications page

    # ==============================================================================
  

    # *******************************************************

    path('jobs/post/', views.post_job_view, name='post_job'),  # URL to post a job
    path('jobs/', views.job_posts_view, name='job_posts'),  # URL to view job posts
    

  ]


