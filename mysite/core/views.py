from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

import pickle
import numpy as np

from mysite.core.forms import SignUpForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def info(request):
    if request.method == 'POST':
        car = request.POST.get('car')
        house = request.POST.get('property')
        income = request.POST.get('income')
        profession = request.POST.get('profession')
        education = request.POST.get('education')

        with open('my_algo.pkl', 'rb') as f:
            kmeans = pickle.load(f)

        data = np.array([[int(car), int(house), int(income), int(profession), int(education)]])
        answer = kmeans.predict(data)
        if answer[0] == 1:
            return render(request, 'approved.html')
        elif answer[0] == 0:
            return render(request, 'reject.html')

    context = {}
    return render(request, 'info.html', context)
