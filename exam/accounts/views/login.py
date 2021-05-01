from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import MyUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

# Create your views here.
def login_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webapp:product_list')
        context['has_error'] = True
    return render(request, 'login.html', context=context)


@login_required
def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('webapp:product_list')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            return redirect('webapp:product_list')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})