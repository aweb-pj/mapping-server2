from django.shortcuts import render
from django.http import HttpResponse
from action.models import *
from action.Serializers import *
import json

import os
# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    print('come to login')
    user_id = request.POST['user_id']
    password = request.POST['password']
    user = User.objects.filter(id = user_id,password = password)
    tmp = User.objects.all()[0]
    print(tmp.id)
    if(len(user)==0):
        status = '400'
    else:
        status = '200'
    result = {
        'status':status
    }

    return HttpResponse(objectToJson(result))

def register(request):
    print('come to register')
    user_id = request.POST['user_id']
    print(user_id)
    password = request.POST['password']
    users = User.objects.filter(id = user_id,password = password)
    if(len(users)!=0):
        status = '400'
    else:
        user = User(id = user_id,password = password)
        user.save()
        status = '200'
    result = {
        'status': status
    }
    return HttpResponse(objectToJson(result))

def addClass(request):
    teacher_id = request.POST['teacher_id']
    class_id = request.POST['class_id']
    teachers = User.objects.filter(id=teacher_id)
    if (len(teachers) == 0):
        status = '400'
    else:
        teacher = teachers[0]
        classes = Clazz.objects.filter(teacher = teacher,id = class_id)
        if(len(classes)!=0):
            status = '400'
        else:
            clazz = Clazz(teacher = teacher,id = class_id)
            clazz.save()
            status = '200'
    result = {
        'status': status
    }
    return HttpResponse(objectToJson(result))

def getTeacherClass(request):
    teacher_id = request.POST['teacher_id']
    print(teacher_id)
    teachers = User.objects.filter(id = teacher_id)
    if(len(teachers) == 0):
        status = '400'
        data = []
        print('teacher is 0')
    else:
        classList = Clazz.objects.filter(teacher = teachers[0])
        if(len(classList) == 0):
            status = '400'
            print('class is 0')
            data = []
        else:
            status = '200'
            data = ClazzSerializer.toClassList(classList)

    result = {
        'status':status,
        'data':data
    }
    return HttpResponse(objectToJson(result))

def updateClass(request):
    teacher_id = request.POST['teacher_id']
    class_id = request.POST['class_id']
    teachers = User.objects.filter(id=teacher_id)
    if (len(teachers) == 0):
        status = '400'
    else:
        teacher = teachers[0]
        classes = Clazz.objects.filter(teacher = teacher,id = class_id)
        if(len(classes)==0):
            status = '400'
        else:
            clazz = Clazz(teacher = teacher,id = class_id)
            clazz.save()
            status = '200'
    result = {
        'status': status
    }
    return HttpResponse(objectToJson(result))

def addTree(request):
    class_id = request.POST['class_id']
    tree_id = request.POST['tree_id']
    classes = Clazz.objects.filter(id=class_id)
    if (len(classes) == 0):
        status = '400'
    else:
        clazz = classes[0]
        trees = Tree.objects.filter(clazz=clazz,id = tree_id)
        if (len(trees) != 0):
            status = '400'
        else:
            status = '200'
            tree = Tree(clazz = clazz,id = tree_id)
            tree.save()

    result = {
        'status': status
    }
    return HttpResponse(objectToJson(result))

def getTree(request):
    class_id = request.POST['class_id']
    classes = Clazz.objects.filter(id = class_id)
    if(len(classes) == 0):
        status = '400'
        data = []
    else:
        trees = Tree.objects.filter(clazz = classes[0])
        if(len(trees) == 0):
            status = '400'
            data = []
        else:
            status = '200'
            data = TreeSerializer.toTreeList(trees)

    result = {
        'status':status,
        'data':data
    }
    return HttpResponse(objectToJson(result))

def updateTree(request):
    class_id = request.POST['class_id']
    tree_id = request.POST['tree_id']
    classes = Clazz.objects.filter(id=class_id)
    if (len(classes) == 0):
        status = '400'
    else:
        clazz = classes[0]
        trees = Tree.objects.filter(clazz=clazz, id=tree_id)
        if (len(trees) == 0):
            status = '400'
        else:
            status = '200'
            tree = Tree(clazz=clazz, id=tree_id)
            tree.save()

    result = {
        'status': status
    }
    return HttpResponse(objectToJson(result))

def chooseClass(request):
    class_id = request.POST['class_id']
    student_id = request.POST['student_id']
    classes = Clazz.objects.filter(id=class_id)
    if (len(classes) == 0):
        status = '400'
    else:
        students = User.objects.filter(id = student_id,role = 'STUDENT')
        if (len(students) == 0):
            status = '400'
        else:
            status = '200'
            chooseclass = ChooseClass(clazz_id = class_id,student_id = student_id)
            chooseclass.save()
    result = {
        'status': status
    }
    return HttpResponse(objectToJson(result))

def getStudentClass(request):
    student_id = request.POST['student_id']
    students = User.objects.filter(id=student_id)
    if (len(students) == 0):
        status = '400'
        data = []
        print('student is 0')
    else:
        status = '200'
        chooseClassList = ChooseClass.objects.filter(student_id = student_id)
        data = ChooseClassSerializer.getClassList(chooseClassList)

    result = {
        'status': status,
        'data': data
    }
    return HttpResponse(objectToJson(result))

def getChooseStudent(request):
    class_id = request.POST['class_id']
    classes = Clazz.objects.filter(id=class_id)
    if (len(classes) == 0):
        status = '400'
        data = []
    else:
        status = '200'
        chooseClassList = ChooseClass.objects.filter(clazz_id = classes[0].id)
        data = ChooseClassSerializer.getStudentList(chooseClassList)

    result = {
        'status': status,
        'data': data
    }
    return HttpResponse(objectToJson(result))