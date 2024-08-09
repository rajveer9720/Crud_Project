from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import AddStudent

# This function add Student and Show Data of Sudents
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['password']
      reg = AddStudent(name=nm, email=em, password=pw)
      reg.save()
    else:
     fm = StudentRegistration()
    stud = AddStudent.objects.all()
    return render(request, "myWebSite/add&show.html",{'form':fm,'stu':stud})

#This Function is update the data of Student
def update_student(request,id):
  if request.method =='POST':
    pi = AddStudent.objects.get(pk=id)
    fm =StudentRegistration(request.POST, instance=pi)
    if fm.is_valid():
     fm.save()
  else:
    pi = AddStudent.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)
  return render(request,'myWebSite/UpdateStudent.html',{'form':fm})

 #This Function delete the Data of Students
def Del_student(request,id):
  if request.method =='POST':
    pi = AddStudent.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')
