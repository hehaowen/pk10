import datetime
import os

import pytz
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from index.models import *


def index(request):
    pk = PK10.objects.all().last()
    odds = Odds.objects.all().last()
    sq = pytz.timezone('Asia/Shanghai')
    time = (datetime.datetime.now(sq)).strftime('%H:%M:%S')
    context = {'pk': pk, 'odds': odds,'time':time}
    return render(request, 'pk10.html', context)


def register(request):
    if request.method == 'POST':
        post = request.POST
        account = post.get('account')
        password1 = post.get('password1')
        password2 = post.get('password2')
        name = post.get('name')
        if password1 == password2:
            user = User(account=account, password=password1, name=name)
            user.save()
        return HttpResponse('注册成功')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        post = request.POST
        account = post.get('account')
        user = User.objects.get(account=account)
        password = post.get('password1')
        if password == user.password:
            request.session['account'] = account
            return HttpResponse('登录成功')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
