from django.shortcuts import render,redirect
from .models import Category, Post
from .forms import CommentForm

def homeView(request):
    posts = Post.objects.all()
    context={
        'posts_set':posts
    }
    return render(request, 'home.html', context)

def detailView(request, slug, pk):
    post=Post.objects.get(slug=slug, pk=pk)

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.post=post
            obj.save()
            return redirect('detail_url',title=post.slug)
    else:
        form=CommentForm()

    context={
        'post_detail':post,
        'form_detail':form,
        'id':pk
    }
    return render(request,'detail.html', context)


def categoryView(request, slug):
    category=Category.objects.get(slug=slug)
    context={
        'category_pair':category
    }
    return render(request,'category.html', context)



