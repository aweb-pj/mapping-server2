# mapping-server API
## /mapping/register
### request
``` json
        {
            'user_id' : 'pj',
            'password' : '1234'
        }
```

### response
* failed
``` json
    {
        'status':'400'
    }
```

* success
``` json
    {
        'status':'200'
    }
```

## /mapping/login
### request
``` json
        {
            'user_id' : 'pj',
            'password' : '1234'
        }
```

### response
* failed
``` json
    {
        'status':'400'
    }
```

* success
``` json
    {
        'status':'200'
    }
```

## /mapping/addClass
### request
``` json
        {
           'class_id': 'class1',
            'teacher_id': 'pj'
        }
```

### response
* failed
``` json
    {
        'status':'400',
    }
```

* success
``` json
    {
        'status':'200',
    }
```

## /mapping/getClass/teacher
### request
``` json
        {
            'teacher_id': 'pj'
        }
```

### response
* failed
``` json
    {
        'status':'400',
        'data':[]
    }
```

* success
``` json
    {
        'status':'200',
        'data':[
            {'id':'class1'},{'id':'class2'},……
            ]
    }
```

## /mapping/addTree
### request
``` json
        {
           'class_id': 'class1',
            'tree_id': 'tree1'
        }
```

### response
* failed
``` json
    {
        'status':'400',
    }
```

* success
``` json
    {
        'status':'200',
    }
```

## /mapping/getTree
### request
``` json
        {
            'class_id': 'class1'
        }
```

### response
* failed
``` json
    {
        'status':'400',
        'data':[]
    }
```

* success
``` json
    {
        'status':'200',
        'data':[
            {'id':'tree1'},{'id':'tree2'},……
            ]
    }
```

## /mapping/chooseClass
### request
``` json
        {
            'class_id': 'class1',
            'student_id':'pj'
        }
```
### response
* success
``` json
    {
        'status':'200',
    }
```

* failed
``` json
    {
        'status':'400',
    }
```

## /mapping/getClass/student
### request
``` json
        {
            'student_id':'pj'
        }
```
### response
* success
``` json
    {
        'status':'200',
        'data':[
            {'id':'class1'},{'id':'class2'},……
            ]
    }
```
* failed
``` json
    {
        'status':'400',
        'data':[]
    }
```
## /mapping/getChooseStudent
``` json
        {
            'class_id': 'class1',
        }
```
### response
* success
``` json
    {
        'status':'200',
        'data':[
            {'id':'student1''},{'id':'student2'},……
            ]
    }
```
* failed
``` json
    {
        'status':'400',
        'data':[]
    }
```
