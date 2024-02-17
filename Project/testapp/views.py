from django.shortcuts import render,HttpResponseRedirect
from testapp.forms import UserForm,ProfileForm,VideoDataForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

@login_required
def features_view(request):
    return render(request, 'pages/features.html')


def upload_videoView(request):
    form = VideoDataForm()
    if request.method == 'POST':
        form = VideoDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Video data saved")
    else:
        form = VideoDataForm()
    return render(request, 'pages/upload_video.html', {'form': form})







def signup_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print('added successfully')
            return HttpResponseRedirect(reverse('testapp:login'))
    else:
        form = UserForm()
    return render(request, 'pages/signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/accounts/home/') 
                return redirect(next_url)
    return render(request, 'pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('testapp:home'))
    # return HttpResponseRedirect(reverse('testapp:logout'))

                                         
