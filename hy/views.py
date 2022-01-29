from django.shortcuts import render, redirect, HttpResponse
from hy.models import Contact
# from hy.models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def some(request):
    return render(request, 'some.html')


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('/login')


# def stu(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         roll = request.POST['roll']
#         email = request.POST['email']
#         password = request.POST['password']
#         phone = request.POST['phone']
#         gender = request.POST['gender']
#         meassge = request.POST['meassge']

#         stu = Student(name=name, roll=roll, email=email,
#                       password=password, phone=phone, gender=gender, meassge=meassge)
#         stu.save()

#     return render(request, 'student.html')


def about(request):
    return render(request, 'about.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST.get('email')
        phone = request.POST['phone']
        meassge = request.POST['meassge']

        contact = Contact(name=name, email=email, phone=phone, meassge=meassge)
        contact.save()

    return render(request, 'contactus.html')


def degin(request):

    return render(request, 'degin.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('/login')


def singup(request):
    return render(request, 'singup.html')


def createuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password1 = request.POST['password']
        password2 = request.POST['re_password']

        if password1 != password2:
            return HttpResponse('password dont match')

        new = User.objects.create_user(
            username=username, email=email, password=password1)
        new.first_name = first_name
        new.last_name = last_name
        new.save()
    return redirect('/login')


# Create your views here.
