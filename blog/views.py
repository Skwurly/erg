from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.

def index(request):
    posts = post.objects.order_by('id').reverse()
    return render(request, 'blog/posts.html', {'posts':posts})
