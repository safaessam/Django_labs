from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from student.forms import MyStudentForm2, MyUserForm,MyStudentForm, MyUserForm2
from student.models import MyUser, Student
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views import View
def home(request):
    if request.session.get("email"):
        students = Student.objects.all()
        context = {}
        context['students'] = students
        return render(request, 'student/home.html', context)
    else:
        return redirect("signin")

def contact(request):
    return render(request, 'student/contact.html')

def about(request):
    return render(request, 'student/about.html')

def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'student/signup.html')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']
        name = request.POST['name']

        if_val = MyUser.objects.filter(email=email)
        if if_val:
            return render(request, 'student/signup.html')

        User.objects.create_user(username=name, email=email, password=password)
        MyUser.objects.create(email=email, password=password, name=name)
        return redirect("signin")

def signin(request):
    if request.method == 'GET':
        return render(request, 'student/login.html')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']

        myuser = MyUser.objects.filter(email=email)

        if myuser:
            auth = authenticate(username=myuser[0].name, password=password)

            if auth:
                login(request, auth)
                request.session["email"] = email
                return redirect("home")
            else:
                return render(request, 'student/login.html')
        else:
            return render(request, 'student/login.html')

def create_student(request):
    if request.method == 'GET':
        return render(request, 'student/create_student.html')

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        age = request.POST['age']

        Student.objects.create(f_name=f_name, l_name=l_name, age=age)

        return redirect('home')

def update_student(request, id):
    student = Student.objects.get(id=id)
    context = {'student': student}

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        age = request.POST['age']

        student.f_name = f_name
        student.l_name = l_name
        student.age = age
        student.save()

        return redirect('home')

    return render(request, 'student/update_student.html', context)

def signout(request):
    request.session.clear()
    logout(request)
    return redirect('signin')
def User_Form(request):
    context = {}
    context['form'] = MyUserForm()

    if request.method == 'GET':
        return render(request, 'student/User_Form.html', context)

    if request.method == 'POST':
        form = MyUserForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            name = request.POST['name']
            password = request.POST['password']

            User.objects.create_user(email=email, username=name, password=password)
            MyUser.objects.create(email=email, name=name, password=password)

        return render(request, 'student/User_Form.html', context)


def Student_Form(request):
    context = {}
    context['form'] = MyStudentForm()

    if request.method == 'GET':
        return render(request, 'student/Student_Form.html', context)

    if request.method == 'POST':
        form = MyStudentForm(request.POST)

        if form.is_valid():
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            age = request.POST['age']

            Student.objects.create(f_name=f_name, l_name=l_name, age=age)

        return render(request, 'student/Student_Form.html', context)
    
    
    
@require_http_methods(['GET', 'POST'])
def User_Form2(request):
    context = {}
    context['form'] = MyUserForm2()

    if request.method == 'GET':
        return render(request, 'student/User_Form.html', context)

    if request.method == 'POST':
        form = MyUserForm2(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submitted successfully')  
        return HttpResponse('Invalid form')  

def Student_Form2(request):
    context = {}
    context['form'] = MyStudentForm2()

    if request.method == 'GET':
        return render(request, 'student/Student_Form.html', context)

    if request.method == 'POST':
        form = MyStudentForm2(request.POST)

        if form.is_valid():
           # f_name = request.POST['f_name']
            #l_name = request.POST['l_name']
            #age = request.POST['age']

          #  Student.objects.create(f_name=f_name, l_name=l_name, age=age)
         form.save()
        return render(request, 'student/Student_Form.html', context)
    




class StudentClassView(View):
    def get(self, request):
        context = {}
        context['form'] = MyStudentForm2()
        return render(request, 'student/Student_Form.html', context)

    def post(self, request):
        form = MyStudentForm2(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student/Student_Form.html', {'form': form})
        else:
            context = {'form': form} 
            return render(request, 'student/Student_Form.html', context)
 

 

class UserClassView(View):
    def get(self, request):
        context = {}
        context['form'] = MyUserForm2()
        return render(request, 'student/User_Form.html', context)

    def post(self, request):
        form = MyUserForm2(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submitted successfully')
        return HttpResponse('Invalid form')