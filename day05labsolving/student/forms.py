from django import forms

from student.models import MyUser, Student

class  MyUserForm(forms.Form):
     name = forms.CharField(max_length=50,required=True)
     email=forms.EmailField(max_length=50,required=True)
     password = forms.CharField(max_length=20,required=True)


class  MyStudentForm(forms.Form):
      id=forms.IntegerField()
      f_name=forms.CharField(max_length=50,required=True)
      l_name=forms.CharField(max_length=50,required=True)
      age=forms.IntegerField()



class MyUserForm2(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'


class MyStudentForm2(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'