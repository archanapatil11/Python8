Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #type function
>>> a=10
>>> type(a)
<class 'int'>
>>> b=3.5
>>> type(b)
<class 'float'>
>>> c=4+3j
>>> type(c)
<class 'complex'>
>>> #type casting
>>> int(a)
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> complex(b)
(3.5+0j)
>>> import math
>>> math.pi
3.141592653589793
>>> math.factorial(7)
5040
>>> import random
>>> random.random(10,20)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    random.random(10,20)
TypeError: Random.random() takes no arguments (2 given)
>>> import random
>>> random.random()
0.0755893542115601
>>> a=[5,6,7,3,2]
>>> random.shuffle(a)
>>> print(a)
[7, 6, 3, 5, 2]
>>> random.choice(a)
6
