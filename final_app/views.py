from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from.forms import VideoForm
from.models import Video
# Create your views here.

def video(request):
  # all_video=Video.objects.all()
  lastvideo= Video.objects.last()
  video= lastvideo.video
  form= VideoForm(request.POST or None, request.FILES or None)
  if request.method=="POST":
    form=VideoForm(data=request.POST,files=request.FILES)
  if form.isvalid:
    form.save()
  #     return HttpResponse("Video Uploaded Successfully")
  # else:
  #   form=VideoForm()

  return render(request, 'final_app/index.html',{"form":form,"video":video})

def home(request):
  return render(request,"final_app/index.html")

def signup(request):

  if request.method=="POST":
    # username=request.POST.get("username")   this works the same
    username=request.POST["username"]
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    email=request.POST["email"]
    pass1=request.POST["pass1"]
    pass2=request.POST["pass2"]

    if pass1 != pass2:
      messages.error(request,"Passwords do not match.")

    myuser=User.objects.create_user(username,email,pass1)
    myuser.first_name=fname
    myuser.last_name=lname

    myuser.save()

    messages.success(request, "Your Account has been successfully created.")

    return redirect("success")

  return render(request,"final_app/signup.html")

def signin(request):

  if request.method=="POST":
    username=request.POST["username"]
    pass1=request.POST["pass1"]

    user=authenticate(username=username,password=pass1)

    if user is not None:
      login(request,user)
      fname=user.first_name
      return render(request,"final_app/index.html",{'fname':fname})
    else:
      messages.error(request,"Wrong Credentials")
      return redirect("home")

  return render(request,"final_app/signin.html")

def signout(request):
  logout(request)
  messages.success(request,"Logged Out Successfully")
  return redirect("home")

def success(request):
  return render(request,"final_app/success.html")