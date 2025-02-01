from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import signupform , ProfileForm , UserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from .models import Profile
# Create your views here.

def signup(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/Profile')

    else:
        form=signupform()
    return render (request,'registration/signup.html',context={'form':form})


@login_required
def profile(request):
    profile=Profile.objects.get(user=request.user)
    print(profile.user.first_name)  # Debugging line
    return render(request,'accounts/profile.html',context={'profile':profile})




def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,request.FILES,instance=request.user)
        profileform=ProfileForm(request.POST,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})