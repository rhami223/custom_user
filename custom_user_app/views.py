from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationsForm, LoginForm
from .models import CustomUser
from django.conf import settings
# Create your views here.

def signupview(request):
    
    if request.method == "POST":
        form = CustomUserCreationsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(username=data.get('username'), password=data.get("password"))
            breakpoint()
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = CustomUserCreationsForm()
    return render(request, "generic_forms.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"),password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))
                )

    form = LoginForm()
    return render(request, "generic_forms.html", {"form": form})


def logout_view(request):
    logout(request)    
    return HttpResponseRedirect(reverse("homepage"))

def index(request):
    return render(request, "index.html", {"display": settings.AUTH_USER_MODEL})

