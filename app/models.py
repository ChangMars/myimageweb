from django.db import models
from django.utils import timezone

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)