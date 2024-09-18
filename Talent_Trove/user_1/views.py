from django.shortcuts import render
def home_view(request):
    return render(request, 'user_1/home.html')

def profile_view(request):
    return render(request, 'user_1/profile.html')

def search_view(request):
    return render(request, 'user_1/search.html')  

def messages_view(request):
    return render(request, 'user_1/messages.html')  

def notifications_view(request):
    return render(request, 'user_1/notifications.html')  

def login_view(request):
    return render(request, 'user_1/login.html')  

def register_view(request):
    return render(request, 'user_1/register.html')  
