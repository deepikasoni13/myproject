from django.shortcuts import render, redirect
from . models import Employee

# Create your views here.
def index(request):
    emp=Employee.objects.all()         # select*from employee
    dictemp={"emp":emp}
    return render(request,"index.html",dictemp)
def registration(request):
    return render(request,"registration.html")
def regcode(request):
    empid=request.POST['empid']
    empname=request.POST['empname']
    department=request.POST['department']
    salary=request.POST['salary']
    emp=Employee()
    emp.empid=empid
    emp.empname=empname
    emp.department=department
    emp.salary=salary
    emp.save()
    return redirect('index')
def delemp(request,id):
    emp=Employee.objects.get(empid=id)
    emp.delete()
    return redirect('index')
def viewemp(request,id):
    emp=Employee.objects.get(empid=id)
    print(emp.empid,emp.empname,emp.department,emp.salary)
    return render(request,"viewemp.html",{"emp":emp})
def updateemp(request):
    empid=request.POST['empid']
    empname=request.POST['empname']   
    department=request.POST['department']
    salary=request.POST['salary']
    Employee.objects.filter(empid=empid).update(empname=empname,department=department,salary=salary)
    return redirect('index')