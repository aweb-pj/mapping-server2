import json
from action.models import *

def objectToJson(obj):
    return json.dumps(obj,ensure_ascii=False)

class ClazzSerializer:
    @staticmethod
    def toClassList(classList):
        array = []
        for clazz in classList:
            item = {
                'id':clazz.id
            }
            array.append(item)
        return array

class TreeSerializer:
    @staticmethod
    def toTreeList(treeList):
        array = []
        for tree in treeList:
            item = {
                'id':tree.id
            }
            array.append(item)
        return array

class ChooseClassSerializer:
    @staticmethod
    def getClassList(chooseClassList):
        array = []
        for chooseClass in chooseClassList:
            item = {
                'id': chooseClass.clazz_id
            }
            array.append(item)
        return array

    @staticmethod
    def getStudentList(chooseClassList):
        array = []
        for chooseClass in chooseClassList:
            item = {
                'id': chooseClass.student_id
            }
            array.append(item)
        return array