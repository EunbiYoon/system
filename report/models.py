from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='  1) Categories'

class Post(models.Model):
    category=models.ForeignKey(Category, related_name='post_model', on_delete=models.CASCADE)
    slug=models.SlugField()
    author=models.ForeignKey(User, related_name='post_user',on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.category)+ ' | ' + str(self.title)
    class Meta:
        verbose_name_plural='  2) Posts'


class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comment_model', on_delete=models.CASCADE)
    author=models.ForeignKey(User, related_name='comment_user',on_delete=models.CASCADE)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.post)+ ' | ' + str(self.body)
    class Meta:
        verbose_name_plural='  3) Comments'