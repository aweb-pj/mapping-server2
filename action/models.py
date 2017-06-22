from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    USER_ROLES = (
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
    )
    role = models.CharField(max_length=7, choices=USER_ROLES)
    def __str__(self):
        return 'id:'+str(self.id)

class ChooseClass(models.Model):
    id = models.IntegerField(primary_key=True, db_column='FId')
    student_id = models.CharField(max_length=100)
    clazz_id = models.CharField(max_length=100)

class Clazz(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    teacher = models.ForeignKey('User',on_delete=models.CASCADE,related_name='teacher',default=None)
    def __str__(self):
        return 'id:'+str(self.id)

class Tree(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    clazz = models.ForeignKey('Clazz',on_delete=models.CASCADE,related_name='trees',default=None)
    def __str__(self):
        return 'id:'+str(self.id)