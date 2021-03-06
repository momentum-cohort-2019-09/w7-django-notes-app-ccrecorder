from django.db import models
from django.utils import timezone
# Create your models here.

class Note(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Put your shit here.", 
        blank=True, 
        null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)    
    
    def __str__(self):
        return self.title

    def update(self):
        self.update_at = timezone.now()
        self.save