from django.shortcuts import render
from django.views.generic import ListView,DetailView
from Blog.models import Post
#from django.http import HttpResponse
# Create your views here.

#example
# posts = [
#     {
#         'author' : 'Mohana',
#         'title': 'Blog Post 1',
#         'content':'First post content',
#         'date_posted':'Sept 20,2021'
#     },
#     {   'author' : 'Sai',
#         'title': 'Blog Post 2',
#         'content':'second post content',
#         'date_posted':'Sept 21,2021'

#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'Blog/home.html', context)

class PostListView(ListView):
    model = Post 
    template_name = 'Blog/home.html'  #<appname>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post 

def about(request):
    return render(request,'Blog/about.html',{'title':'About'})
