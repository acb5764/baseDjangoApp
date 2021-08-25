from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            # check if form is valid in backend django, if so then get the username
            form.save()
            # automatically handles password hashing and storage via the database, super simple
            username = form.cleaned_data.get('username')
            # success message
            messages.success(request, f'Your account has been created. {username} is now able to login!')
            # add redirect
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required #this is a decorator, makes access to the view require authorization
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile') #to avoid "form resubmission warning"

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form' : u_form, 
        'p_form' : p_form
    }

    return render(request, 'users/profile.html', context)

# Create your views here.

# messages.debug
# messages.info
# messages.success
# messages.WARNING
# messages.error
