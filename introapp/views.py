from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  
            return redirect('introapp:user_created', user_id=user.id)
    else:
        form = UserForm()
    return render(request, 'introapp/create_user.html', {'form': form})

def user_created(request, user_id):
    user = get_object_or_404(User, id=user_id)  
    return render(request, 'introapp/user_created.html', {'user': user})

def success(request):
    return render(request, 'introapp/success.html')


def user_list(request):
    users = User.objects.all()  
    return render(request, 'introapp/user_list.html', {'users': users})