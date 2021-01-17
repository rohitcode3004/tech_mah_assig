from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
	    form = UserRegisterForm()
    return render(request, 'users/create.html', {'form': form})


def index(request):
    users = User.objects.all()
    #form = UserRegisterForm()

    context = {'users': users}
    return render(request, 'users/list.html', context)


def updateUser(request, pk):
	user = User.objects.get(id=pk)

	form = UserRegisterForm(instance=user)

	if request.method == 'POST':
		form = UserRegisterForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
		return redirect('/users')

	context = {'form':form}
	return render(request, 'users/update_user.html', context)


def profile(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    user = User.objects.get(id=pk)
    u_form = UserUpdateForm(instance=user)
    p_form = ProfileUpdateForm(instance=user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
        }
    return render(request, 'users/profile.html', context)
