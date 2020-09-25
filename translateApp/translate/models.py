from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    user_id = models.IntegerField(blank=False)
    catagory = models.CharField(max_length=100)
    translated = models.BooleanField(default=False)
    content = models.TextField(blank=False)
    language = models.CharField(max_length=50, blank=False)
    level = models.CharField(max_length=50, blank=False)
    word_count = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

