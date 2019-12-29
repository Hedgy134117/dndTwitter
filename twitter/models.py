from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.author.username + ": " + self.content[:10] + "..."

    def snippet(self):
        return self.content[:100] + "..."

class Comment(models.Model):
    content = models.TextField(max_length=255)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.author.username + ": " + self.content[:10] + "..."