import datetime
import random
import string
from datetime import datetime
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from django.contrib import auth
from .forms import TaskForm, StudentForm
from .models import Task, StudentList


def projectHomePage(request):
    return render(request, 'adminApp/ProjectHomePage.html')


def printpagecall(request):
    return render(request, 'adminApp/printer.html')


def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1 = {'user_input': user_input}
    return render(request, 'adminApp/printer.html', a1)


def exceptionpagecall(request):
    return render(request, 'adminApp/ExceptionExample.html')


def exceptionpagelogic(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminApp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminApp/ExceptionExample.html')


def randompagecall(request):
    return render(request, 'adminApp/RandomExample.html')


def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran': ran}
    return render(request, 'adminApp/RandomExample.html', a1)


def otppagecall(request):
    return render(request, 'adminApp/OTPExample.html')


def otplogic(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num))
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminApp/OTPExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminApp/OTPExample.html')


def calculatorpagecall(request):
    return render(request, 'adminApp/Calculator.html')


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminApp/Calculator.html', {'result': result})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminApp/add_task.html', {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')


def calculatormainpagecall(request):
    return render(request, 'adminApp/CalculatorMain.html')


def calculatormainlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminApp/CalculatorMain.html', {'result': result})


def datetimepagecall(request):
    return render(request, 'adminApp/DateTimeExample.html')


def datetimepagelogic(request):
    if request.method == 'POST':
        num1 = int(request.POST['user_input'])
        x = datetime.now()
        print(x + timedelta(days=num1))
        result = x + timedelta(days=num1)
    return render(request, 'adminApp/DateTimeExample.html', {'result': result})


def registerpagecall(request):
    return render(request, 'adminApp/registerPage.html')


def registerpagelogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm_password']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'adminApp/ProjectHomePage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request, 'adminApp/ProjectHomePage.html')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminApp/ProjectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminApp/registerPage.html')
    else:
        return render(request, 'adminApp/registerPage.html')


def loginpagecall(request):
    return render(request, 'adminApp/LoginPage.html')


def loginpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        assert isinstance(user, object)
        auth.login(request, user)
        if user is not None:
            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('studentApp:studentHomePage')
            elif len(username) == 4:
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyApp:facultyHomePage')
            else:
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminApp/LoginPage.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminApp/LoginPage.html')
    else:
        return render(request, 'adminApp/LoginPage.html')


def logout(request):
    auth.logout(request)
    return redirect('ProjectHomePage')


# def addStudent(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('studentList')
#     else:
#         form = StudentForm()
#     return render(request, 'adminApp/AddStudent.html', {'form': form})


from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminApp/AddStudent.html', {'form': form})
            student.save()
            return redirect('studentList')
    else:
        form = StudentForm()
    return render(request, 'adminApp/AddStudent.html', {'form': form})

def studentList(request):
    students = StudentList.objects.all()
    return render(request, 'adminApp/StudentList.html', {'students': students})


from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Monthly Sales Distribution')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request, 'adminApp/Chart.html',
                      {'total_sales': total_sales,
                       'average_sales': average_sales,
                       'chart': image_data})
    return render(request, 'adminApp/Chart.html', {'form': UploadFileForm()})


from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')

        feedback = Feedback(name=name, phone=phone, email=email, description=description)
        feedback.save()

        return render(request, 'adminapp/feedback_success.html')
    return render(request, 'adminapp/feedback.html')