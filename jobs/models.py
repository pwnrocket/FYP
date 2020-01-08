import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import  get_user_model
# Create your models here.

class Job(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('job_detail',kwargs={'pk':str(self.pk)})



