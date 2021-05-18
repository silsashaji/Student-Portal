from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=160, blank=True)

    faculty = 'faculty'
    student = 'student'
    user_types = [
        (faculty, 'faculty'),
        (student, 'student'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)

    def __str__(self):
        return self.user.username
    
