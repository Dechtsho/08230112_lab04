from django.db import models

# Create your models her

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.full_name


class LearningEntry(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title} ({self.date})"
