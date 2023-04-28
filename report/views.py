from django.shortcuts import render,redirect, get_object_or_404
from .models import Category, Post
from .forms import CommentForm

def homeView(request):
    posts = Post.objects.all()
    context={
        'posts_set':posts
    }
    return render(request, 'home.html', context)

def detailView(request, slug, pk):
    comment_post = get_object_or_404(Post)
    comments = comment_post.comments.filter(active=True)
    new_comment=None

    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.comment_post = comment_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context={
        'post': comment_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'slug':slug,
        'pk':pk
    }
    return render(request,'detail.html', context)

def categoryView(request, slug):
    category=Category.objects.get(slug=slug)
    context={
        'category_pair':category
    }
    return render(request,'category.html', context)



