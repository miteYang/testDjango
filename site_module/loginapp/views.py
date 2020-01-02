from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from loginapp.models import User


def index(request):
    return render(request,'index.html')

def detail(request):
    if request.method=='POST':
        username=request.POST.get('username',None)
        passwd=request.POST.get('passwd',None)
        message='所有字段都必须填写'
        if username and passwd:
            username=username.strip()
            try:
                user=User.user1.get(name=username)
                if user.password==passwd:
                    return render(request,'detail.html')
                else:
                    return render(request,'index.html',{'error':'密码不正确'})
            except:
                return render(request,'index.html',{'error':'账号不存在'})
        else:
            return render(request,'index.html',{'error':'账号或密码为空'})

def mytest(request):
    return render(request,'mytest.html');

def myclick(request):
    str = User.user1.all()
    print(str)
    return render(request,'myresulet.html',{'message':str});