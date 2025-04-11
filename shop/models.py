from django.db import models

class Perfume(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='perfumes/')
    description=models.TextField()
    
    def __str__(self):
        return self.name

# Create your models here.
