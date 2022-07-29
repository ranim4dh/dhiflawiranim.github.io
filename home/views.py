from django.shortcuts import render
from .models import ContactMessage
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    if request.method == "POST":
        contact = ContactMessage()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.message = request.POST['message']
        contact.ip = request.META.get('REMOTE_ADDR')
        contact.save()
        messages.success(
            request, "Your message has ben sent. Thank you for your message.")
    return render(request,'home/index.html',{})

def moviespree(request):
    return render(request,'home/moviespree.html',{})

def doremi(request):
    return render(request,'home/doremi.html',{})

def design(request):
    return render(request,'home/design.html',{})

def tedalel(request):
    return render(request,'home/tedalel.html',{})

def perpro(request):
    return render(request,'home/perpro.html',{})

def shop(request):
    return render(request,'home/dailyshop.html',{})