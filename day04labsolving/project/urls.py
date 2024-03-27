"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import Student_Form, Student_Form2, StudentClassView,User_Form, User_Form2, home, about, contact,delete_student, signin,signup,create_student,update_student,signout,UserClassView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home, name="home" ),
    path("contact/", contact, name="contact" ),
    path("about/", about, name="about" ),
    path("contact/",contact,name="contact"),
    path("delete_student/<int:id>",delete_student,name='delete_student'),
    path("signin/", signin, name="signin" ),
    path("signup/", signup, name="signup" ),
    path("create-student/", create_student, name="create-student"), 
    path('update_student/<int:id>/', update_student, name='update_student'),
     path("signout/", signout, name="signout" ),
     path("User_Form/", User_Form, name="User_Form" ),
    path("Student_Form/", Student_Form, name="Student_Form" ),
    path("User_Form2/", User_Form2, name="User_Form2" ),
    path("Student_Form2/", Student_Form2, name="Student_Form2" ),
   path("StudentClassView/", StudentClassView.as_view(), name="StudentClassView"), 
     path("UserClassView/", UserClassView.as_view(), name="UserClassView"), 







]
