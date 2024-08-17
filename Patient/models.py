from django.db import models

# Create your models here.
class UserRegister(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    n='select gender'
    g = [
        (None, 'select gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender=models.CharField(max_length=12,choices=g,default=None)
    age=models.IntegerField()
    address=models.TextField()
    phnNo=models.IntegerField(default='',verbose_name='Contact_No')
    def __str__(self):
        return self.email
    
class UserFeedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    feedback=models.TextField()
    date=models.DateField(auto_created=True,auto_now=True)

    def __str__(self):
        return self.name
    