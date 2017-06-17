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
    teacher_id = request.POST['teacher_id']
    password = request.POST['password']
    teachers = Teacher.objects.filter(id = teacher_id,password = password)
    tmp = Teacher.objects.all()[0]
    print(tmp.id)
    if(len(teachers)==0):
        status = '400'
    else:
        status = '200'
    result = {
        'status':status
    }

    return HttpResponse(objectToJson(result))

def register(request):
    print('come to register')
    teacher_id = request.POST['teacher_id']
    print(teacher_id)
    password = request.POST['password']
    teachers = Teacher.objects.filter(id = teacher_id,password = password)
    if(len(teachers)!=0):
        status = '400'
    else:
        teacher = Teacher(id = teacher_id,password = password)
        teacher.save()
        status = '200'
    result = {
        'status': status
    }
    return HttpResponse(objectToJson(result))

def addClass(request):
    teacher_id = request.POST['teacher_id']
    class_id = request.POST['class_id']
    teachers = Teacher.objects.filter(id=teacher_id)
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

def getClass(request):
    teacher_id = request.POST['teacher_id']
    print(teacher_id)
    teachers = Teacher.objects.filter(id = teacher_id)
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
    teachers = Teacher.objects.filter(id=teacher_id)
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