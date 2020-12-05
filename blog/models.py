from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	body = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/')



	