from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('shop_views-home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
