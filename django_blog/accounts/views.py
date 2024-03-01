from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def log_in(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('posts:posts_list')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/log_in.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:posts_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:posts_list')