from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from app1 import views
def home(request):
    if request.method =='POST':
        stud_name = request.POST['stud_name']
        Gender=request.POST['Gender']
        Department=request.POST['Department']
        email=request.POST['email']
        if len(stud_name)<3:
            return HttpResponse('<h1> Please enter properly student name</h1')
        else:
            Stud_list=Student(stud_name=stud_name,Gender=Gender,Department=Department,email=email)
            Stud_list.save()
            return render(request, 'home.html', {'message': 'The student has been registered successfully.'})
    # stud_list = Student.obejects.all()
    # context={'stud_list':stud_list}
    return render(request,'home.html',{})
    # return HttpResponse('<h1> This is our first test django project</h1')
# Create your views here.
