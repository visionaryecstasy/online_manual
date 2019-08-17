from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Manual(models.Model):
    title = models.CharField(max_length=32, default=" ")
    category = models.CharField(max_length=100, default=" ")
    context = RichTextUploadingField(max_length=10000,default=" ")

    def __str__(self):
        return self.title

class Message(models.Model):
    username = models.CharField(max_length=256)
    content = models.TextField(max_length=1000)
    publish = models.DateTimeField()

    #for demonstrate
    def __str__(self):
        notification = '<Message:[username:{username}, content:{content},publish:{publish}]'
        return notification.format(username=self.username, content =self.content, publish = self.publish)

class comment(models.Model):
    comment_user = models.CharField(max_length=20)
    To_user = models.CharField(max_length=20)
    words = models.TextField(max_length=400, null=False)
    Time = models.DateTimeField()
