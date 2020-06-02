from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.views.generic import (ListView,CreateView)

# Create your views here.
class PostListView(ListView):
    template_name = 'Insta/post_list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name ='Insta/post_create.html'
    from_class = PostForm
    queryset = Post.objects.all()


    def form_valid(self, form):
        print(form.claned_data)
        form.Instance.author = self.request.user
        return super().form_valid(form)