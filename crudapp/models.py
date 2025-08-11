from django.db import models
# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField(default='2000-02-02')
    department=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    def __str__(self):
        return self.name
        