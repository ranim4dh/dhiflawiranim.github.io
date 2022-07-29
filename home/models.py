from django.db import models

# Create your models here.

    
class ContactMessage(models.Model):
   
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)
    ip = models.CharField(blank=True, max_length=20)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name