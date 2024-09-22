from django.shortcuts import render, redirect,get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ---------------------------------------------------------------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after registration
    else:
        form = UserRegistrationForm()

    return render(request, 'user_1/register.html', {'form': form})
  
# ---------------------------------------------------------------------------------


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page after login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'user_1/login.html')
 
# ---------------------------------------------------------------------------------

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login or home page
    return redirect('login')  # Redirect to home or any other page if not POST


#----------------------------------------------------------------------------------

def home_view(request):
    return render(request, 'user_1/home.html')


# ---------------------------------------------------------------------------------


from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def profile_view(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    posts = ImagePost.objects.all()  # Fetch posts here
    
    # Handle Profile form
    if request.method == 'POST' and 'profile_form' in request.POST:
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm(instance=user_profile)
    
    # Handle Job Post form
    job_form = JobPostForm()

    context = {
        'user_profile': user_profile,
        'form': form,
        'posts': posts,  # Pass posts here
        'job_form': job_form,  # Add JobPostForm to context
    }
    return render(request, 'user_1/profile.html', context)


# ---------------------------------------------------------------------------------


def search_view(request):
    return render(request, 'user_1/search.html')  

# ---------------------------------------------------------------------------------

def messages_view(request):
    return render(request, 'user_1/messages.html')  

# ---------------------------------------------------------------------------------


def notifications_view(request):
    return render(request, 'user_1/notifications.html')  

# **********************************************************************************

from .models import ImagePost
from .forms import ImagePostForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import ImagePost
from .forms import ImagePostForm

# View for displaying the user's gallery
def gallery_view(request):
    if request.user.is_authenticated:
        posts = ImagePost.objects.filter(user=request.user).order_by('-created_at')
    else:
        posts = ImagePost.objects.none()  # No posts if the user is not authenticated
    
    return render(request, 'user_1/profile/media_hub.html', {'posts': posts})

# View for adding a new post
def add_post_view(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image_post = form.save(commit=False)
            image_post.user = request.user  # Assign the logged-in user to the post
            image_post.save()
            return redirect('profile')  # Redirect to profile after successful form submission
    else:
        form = ImagePostForm()
    return render(request, 'user_1/profile/add_post.html', {'form': form})

# View for editing a post
def edit_post_view(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id, user=request.user)  # Ensure the user is authorized to edit the post

    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()  # Save the edited post
            return redirect('profile')  # Redirect to profile after successful edit
    else:
        form = ImagePostForm(instance=post)  # Populate the form with existing post data
    
    return render(request, 'user_1/profile/add_post.html', {'form': form})

# View for deleting a post
def delete_post_view(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id, user=request.user)  # Ensure the user is authorized to delete the post
    post.delete()
    return redirect('profile')  # Redirect to profile after deletion

# ---------------------------------------------------------------------------------


from django.shortcuts import render, redirect
from .models import JobPost
from .forms import JobPostForm



@login_required
def post_job_view(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.user_profile = request.user.userprofile  # Associate with the user's profile
            job_post.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = JobPostForm()

    return render(request, 'user_1/profile/post_job.html', {'form': form})

# *****************************************************************************



def job_posts_view(request):
    
    jobs = JobPost.objects.all()
    print(jobs)
    return render(request, 'user_1/profile/job_posts.html', {'jobs': jobs})