from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def Home(request):
  stu=Student.objects.all()
  return render(request,'home.html',{"student":stu})
def about(request):
  return render(request,'about.html')


def login(request):
  if request.method == 'POST':
      name =request.POST.get('name')
      age= request.POST.get('age')
      roll_number = request.POST.get('roll_number')
      email = request.POST.get('email')
      stu=Student(name=name, age=age, roll_number=roll_number, email=email)
      stu.save()
      return render(request,'login.html')
    
    
  else:
    return render(request,'login.html') 
def show_details(request):
    if request.method == "POST":
        # Extract form data from POST request
        name = request.POST.get('name')
        age = request.POST.get('age')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        
        context = {
            'name': name,
            'age': age,
            'roll_number': roll_number,
            'email': email
        }
        return render(request, 'show_details.html', context)
    else:
        # If not POST, redirect or show empty page or error
        return render(request,       'show_details.html', {}) 
