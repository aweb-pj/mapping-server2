# mapping-server API
## /mapping/register
### request
``` json
        {
            'teacher_id' : 'pj',
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
            'teacher_id' : 'pj',
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

## /mapping/getClass
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