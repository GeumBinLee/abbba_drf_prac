from django.db import models
from users.models import User

class Article(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(blank=True, upload_to = '%Y/%m/%d/')
    likes = models.ManyToManyField(User, related_name="likes")
    
    def __str__(self) :
        return str(self.title)


class Comment(models.Model) :
    post = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="comment")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self) :
        return str(self.content)