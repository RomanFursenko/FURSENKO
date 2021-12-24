from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.template import loader

from .models import Md

def index(request):
    template = loader.get_template('mydict/index.html')
    mds = Md.objects.order_by('-published')
    context = {'mds' : mds}
    return HttpResponse(template.render(context, request))

def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'mydict/posts.html', {'posts':posts})
