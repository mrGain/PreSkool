from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from app.EmailBackEnd import EmailBackEnd

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request, 'login.html')    

def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user != None:
            login(request, user)
            user_type = user.user_type
            
            if user_type == '1':
                return redirect('hod/home')
            elif user_type == '2':
                return HttpResponse("This is Staff Panel")
            elif user_type == '3':
                return HttpResponse("This is Student Panel")
            else:
                # message
                messages.error(request,"Email or Password is invalid.!")
                return redirect('login')
        else:
                # message
                messages.error(request,"Email or Password is invalid.!")
                return redirect('login')
    else:
        return redirect('login')            
        
# Logout functions startts 
def doLogout(request):        
    logout(request)
    return redirect('login')