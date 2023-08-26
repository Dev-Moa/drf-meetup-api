from django.db import models

# Create your models here.


class MeetUp(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title