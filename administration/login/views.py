from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import tbl_Authentication

# Create your views here.
def base(request):
    return render(request,'base.html')

def dashboard(request):
    return render(request,'dashboard.html')

def Userreg(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Pwd=request.POST['Pwd']
        Age=request.POST['Age']
        Gender=request.POST['Gender']
        Maritalstatus=request.POST['Maritalstatus']
        Newuser(Username=Username,Email=Email,Pwd=Pwd,Gender=Gender,Maritalstatus=Maritalstatus).save()
        messages.success(request,'The new user'+request.POST[username]+'is saved successfully')
        return render(request,registration.html)
    else:
        return render(request,'registration.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=tbl_Authentication.empAuth_objects.get(username=username,password=password)
            if user is not None:
                return render(request,'dashboard.html',{})
            else:
                print('Someone tried to login and failed')
                print("They use username: {} and password: {}".format(username,password))

                return redirect('/')
        except Exception as identifier:

            return redirect('/')

    else:
        return render(request, 'base.html')

