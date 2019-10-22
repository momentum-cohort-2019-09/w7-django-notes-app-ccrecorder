from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=100, blank=False, null=False)
  body = models.TextField(help_text="Your note goes here, YO", blank=False, null=False)
  created_at = models.DateTimeField(default=timezone.now())
  updated_at = models.DateTimeField(blank=True, null=True)
  
  def update(self):
    self.updated_at = timezone.now()
    self.save()
  
  def __str__(self):
    return self.title
