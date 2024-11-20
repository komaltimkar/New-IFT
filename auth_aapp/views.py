from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to dashboard after successful registration
        else:
            return render(request, 'auth/register.html', {'form': form})  # If form is invalid, re-render the register page
    else:
        form = UserCreationForm()  # Initialize an empty form for GET request
    return render(request, 'auth/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            return render(request, 'auth/login.html', {'form': form})  # If form is invalid, re-render the login page
    else:
        form = AuthenticationForm()  # Initialize an empty form for GET request
    return render(request, 'auth/login.html', {'form': form})

# Dashboard View (This should return a dashboard page)
def dashboard_view(request):
    # This is just a placeholder, you can customize it as per your needs
    return render(request, 'auth/dashboard.html')

# Logout View
def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('login')  # Redirect to login page after logging out
