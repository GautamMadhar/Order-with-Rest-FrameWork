from django.db import models

# Create your models here.

class Order(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField()
	address = models.TextField()

	def __str__(self):
		return self.firstname
    
