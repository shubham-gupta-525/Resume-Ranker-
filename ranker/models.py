from django.db import models

# Create your models here.

class JobDescription(models.Model):
    role = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.role

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    score = models.FloatField(default=0)

    def __str__(self):
        return self.file

