from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(max_length=400, blank=True, null=True)
    design = models.BooleanField(default=False, blank=True, null=True)
    developing = models.BooleanField(default=False, blank=True, null=True)
    piloting = models.BooleanField(default=False, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return self.title

