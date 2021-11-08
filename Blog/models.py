from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"


class addPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    description = models.CharField(max_length=100,blank=False,default="N/A")
    image_url = models.CharField(max_length=200,null=True)
    author = models.ForeignKey(User,on_delete=CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.title} {self.timestamp}"

    def serialize(self):
        return{
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "body" : self.body,
            "image" : self.image_url,
            "author" : self.author.username,
            "timestamp":self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }