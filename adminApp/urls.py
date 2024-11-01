from django.urls import path

from . import views

urlpatterns = [
    path('', views.projectHomePage, name='ProjectHomePage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('otppagecall/', views.otppagecall, name='otppagecall'),
    path('otplogic/', views.otplogic, name='otplogic'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('calculatormainpagecall/', views.calculatormainpagecall, name='calculatormainpagecall'),
    path('calculatormainlogic/', views.calculatormainlogic, name='calculatormainlogic'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('registerpagecall/', views.registerpagecall, name='registerpagecall'),
    path('registerpagelogic/', views.registerpagelogic, name='registerpagelogic'),
    path('loginpagecall/', views.loginpagecall, name='loginpagecall'),
    path('loginpagelogic/', views.loginpagelogic, name='loginpagelogic'),
    path('logout/', views.logout, name='logout'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('studentList/', views.studentList, name='studentList'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('submit_feedback', views.feedback_form, name='submit_feedback'),
]
