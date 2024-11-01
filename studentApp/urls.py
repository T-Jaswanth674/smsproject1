from django.urls import path, include
from . import views
app_name = 'studentApp'
urlpatterns = [
    path('studentHomePage/', views.studentHomePage, name='studentHomePage'),
]