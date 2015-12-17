from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import User
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.contrib import messages

def user_login(request):
	if request.method == 'POST':
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None and user.is_active:
				login(request, user)
				return redirect('system.views.user_home')

			else:
				failed = "Login failed!"
				return render(request, 'system/user_login.html', {'failed':failed})

		except User.DoesNotExist:
			failed = "Login Failed!"
			return render(request, 'system/user_login.html', {'failed': failed})

	elif request.user.is_authenticated():
		return redirect('system.views.user_home')

	elif not request.user.is_authenticated():
		return render(request, 'system/user_login.html')

@login_required
def user_home(request):
	user = get_object_or_404(User, pk=request.user.pk)

	if user.is_admin:
		return HttpResponse("Logged in successfully")

	elif not user.is_admin:
		return HttpResponse("ERROR!")	
