from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import Post
from django.urls import reverse
from .models import addPost,User

# Create your views here.

def index(request):
    return render(request,"Blog/home.html")

def aPost(request):
    
    if request.method == "POST":
        form = Post(request.POST,request.FILES)
        if form.is_valid():
           newPost = form.save(commit=False)
           newPost.author = request.user
           newPost.save()
           return HttpResponseRedirect(reverse('index'))
        
    else:
        form = Post()
    return render(request,'Blog/add.html',{
        "form": form
    })

def Posts(request):
    posts  = addPost.objects.order_by("-timestamp").all()
    return JsonResponse([post.serialize() for post in posts], safe=False)

def blogpost(request,blog_id):
    post = addPost.objects.get(pk=blog_id)
    return render(request,'Blog/blogpost.html',{
        "post" : post,
    })