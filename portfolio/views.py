
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ContactMessage

def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    success = False
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            # Save the message inside the DB
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            success = True

    return render(request, 'portfolio/contact.html', {'success': success})
