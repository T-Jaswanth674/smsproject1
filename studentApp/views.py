from django.shortcuts import render


# Create your views here.
def studentHomePage(request):
    return render(request, 'studentApp/StudentHomePage.html')
