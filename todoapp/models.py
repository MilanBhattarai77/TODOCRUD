from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.EmailField()
    phone_number=models.IntegerField()
    address=models.CharField(max_length=200)


    def __str__(self):
        return self.full_name
    
    
class Task(models.Model):
    title=models.CharField()
    completed=models.BooleanField(default=True)
    created_at=models.TimeField(auto_created=True)
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
