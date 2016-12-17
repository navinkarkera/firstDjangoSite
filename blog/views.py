from django.shortcuts import render
from .models import Author, Blog, Entry
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'list_blogs'
    def get_queryset(self):
        return Blog.objects.all()
