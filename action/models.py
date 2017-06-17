from django.db import models

# Create your models here.

class Teacher(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return 'id:'+str(self.id)

class Clazz(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE,related_name='classes')
    def __str__(self):
        return 'id:'+str(self.id)

class Tree(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    clazz = models.ForeignKey('Clazz',on_delete=models.CASCADE,related_name='trees',default=None)
    def __str__(self):
        return 'id:'+str(self.id)