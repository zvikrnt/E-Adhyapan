from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    
class MyProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)

    
class MyVideo(models.Model):
    title = models.CharField(max_length = 100)
    topic = models.ForeignKey(to=Topic, on_delete=CASCADE, null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    uploaded_by = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)
    video = models.FileField(upload_to ="video//" ,null=True, blank=True)
    youtube_link = models.CharField(max_length=200 ,null=True, blank=True)

class VideoLike(models.Model):
    video = models.ForeignKey(to=MyVideo, on_delete=CASCADE, null=True, blank=True)
    liked_by = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)

class Notes(models.Model):
    subject = models.CharField(max_length = 100)
    topic = models.ForeignKey(to=Topic, on_delete=CASCADE, null=True, blank=True)
    uploaded_by = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)
    description = models.TextField()
    attachment = models.FileField(upload_to ="docs//" ,null=True, blank=True)

class Question(models.Model):
    subject = models.CharField(max_length = 100)
    topic = models.ForeignKey(to=Topic, on_delete=CASCADE, null=True, blank=True)
    question = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    asked_by = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)
    answer = models.TextField()

    
