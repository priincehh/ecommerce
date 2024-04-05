from django.shortcuts import render, redirect
from .models import user,prd


# Create your views here.

def log(request):
    return render(request, 'login.html')


def reg(request):
    return render(request, 'registraion.html')


def hom(request):
    data = prd.objects.all()
    for i in data:
        print(i.prd_name)
        return render(request, 'home.html',{'data':data})


    return render(request, 'home.html')


def login_btn(request):
    print('>>>>>>>>>>>>>>>>>>>>')
    if request.method == "POST":
        name = request.POST.get('name')
        pas = request.POST.get('pass')
        print(name)
        print(pas)
        if user.objects.filter(name=name, passw=pas).exists():
            return render(request, 'home.html')

        else:
            return render(request, 'login.html')


def reg_btn(request):
    print('>>>>>>>>>>>>>>>>>>>>')
    if request.method == "POST":
        name = request.POST.get('username')
        pas = request.POST.get('pass')
        email = request.POST.get('email')
        ph = request.POST.get('ph')
        address = request.POST.get('address')
        print(name)
        print(pas)
        print(email)
        print(ph)
        print(address)
        user.objects.create(name=name, passw=pas,email=email, phone=ph, address=address)
        return render(request, 'login.html')

        # if user.objects.filter(name=name, passw=pas).exists():
        #     return render(request, 'home.html')
        #
        # else:
    return render(request, 'registraion.html')
