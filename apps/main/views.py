from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

def index(request):
    print '*'*50
    print 'Main:index'
    print '*'*50
    print " "
    return render(request, 'login/index.html')
