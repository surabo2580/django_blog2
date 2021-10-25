from django.shortcuts import render
from django.http import HttpResponse
from feeds.models import News_Post


# Create your views here.

def homeFeed(request):
    allposts = News_Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'feeds/feedHome.html',context)

def feedPost(request,slug):
    newsPost = News_Post.objects.filter(slug=slug)
    #context = {'newsPost':newsPost}
    print(newsPost)
    return render(request,'feeds/feedPost.html')
