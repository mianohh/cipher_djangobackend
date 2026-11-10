from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact, Employee

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('home')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('home')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully.')
        return redirect('home')

    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(full_name=full_name, email=email, subject=subject, message=message)
        contact.save()

        messages.success(request, 'Message sent successfully.')
        return redirect('contact')


    return render(request, 'contact.html')

def employee(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        position = request.POST.get('position')
        department = request.POST.get('department')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            position=position,
            department=department,
            hire_date=hire_date,
            salary=salary,
        )

        messages.success(request, 'Employee saved successfully.')
        return redirect('employee')

    return render(request, 'employee.html')