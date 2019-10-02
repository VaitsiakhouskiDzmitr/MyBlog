from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from django.views.generic import View




def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts' : posts})



class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post' : post})




# Create your views here.
