from django.db import models
from django.contrib.auth.models import User, Permission

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        permissions = [
            ('recruiter', 'Recruiter Permission'),
        ]

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
