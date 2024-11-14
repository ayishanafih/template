from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact  # Ensure your Contact model is imported
from .models import Contactnew

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):   
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']

        # Save the data to the database
        contact = Contactnew(name=name, email=email, message=message, subject=subject)
        contact.save()

    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

