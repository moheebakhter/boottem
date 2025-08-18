from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"myapp/home.html")

def about(request):
    return render(request,"myapp/about.html")

def contact(request):
    return render(request,"myapp/contact.html")

def Courses(request):
    return render(request,"myapp/Courses.html")

def Dropdown(request):
    return render(request,"myapp/Dropdown.html")

def Events(request):
    return render(request,"myapp/Events.html")

def Pricing(request):
    return render(request,"myapp/Pricing.html")

def Trainers(request):
    return render(request,"myapp/Trainers.html")