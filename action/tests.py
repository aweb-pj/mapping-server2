from django.test import TestCase
from action.models import *
from action.Serializers import *
import json
# Create your tests here.

class MyTest(TestCase):
    def Register(self):
        url = '/mapping/register'
        data = {
            'teacher_id' : 'pj',
            'password' : '1234'
        }
        correct_data = {
            'status':'200'
        }
        response = self.client.post(url, data)
        return_data = json.loads(str(response.content,encoding='utf-8'))
        #print(str(response.content,))
        self.assertEqual(return_data, correct_data)

    def Login(self):
        #self.Register()
        url = '/mapping/login'
        data = {
            'teacher_id':'pj',
            'password':'1234'
        }
        correct_data = {
            'status': '200'
        }
        response = self.client.post(url, data)
        return_data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(return_data, correct_data)

    def testLoginAndLogin(self):
        self.Register()
        self.Login()

    # addClass test
    def AddClass(self):
        url = '/mapping/addClass'
        clazz = {
            'class_id': 'class1',
            'teacher_id': 'pj'
        }
        correct_data = {
            'status': '200'
        }
        response = self.client.post(url, clazz)
        return_data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(return_data, correct_data)

    def GetClass(self):
        #getClass test
        url = '/mapping/getClass'
        data = {
            'teacher_id': 'pj'
        }
        correct_data = {
            'status': '200',
            'data':[
                {'id':'class1'}
            ]
        }
        response = self.client.post(url, data)
        return_data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(return_data, correct_data)

    def testClass(self):
        self.Register()
        self.AddClass()
        self.GetClass()

    def AddTree(self):
        url = '/mapping/addTree'
        tree = {
            'class_id': 'class1',
            'tree_id': 'tree1'
        }
        correct_data = {
            'status': '200'
        }
        response = self.client.post(url, tree)
        return_data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(return_data, correct_data)

    def GetTree(self):
        url = '/mapping/getTree'
        data = {
            'class_id': 'class1'
        }
        correct_data = {
            'status': '200',
            'data':[
                {'id':'tree1'}
            ]
        }
        response = self.client.post(url, data)
        return_data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(return_data, correct_data)

    def testTree(self):
        self.Register()
        self.AddClass()
        self.AddTree()
        self.GetTree()


