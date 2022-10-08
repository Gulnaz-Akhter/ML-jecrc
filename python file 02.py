Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='white'
b="white"
c='''white'''
print(c)
white
print(b)
white
a='hello world'
print(a)
hello world
a[0]
'h'
a[6]
'w'
a[4]
'o'
a[10]
'd'
a[-1]
'd'
a[1],[2]
('e', [2])
a[[1],[2]]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[[1],[2]]
TypeError: string indices must be integers
a=[0:2]
SyntaxError: invalid syntax
a='hello world'
a[0:2]
'he'

a[0:2:1:3]
SyntaxError: invalid syntax
a[0:2]
'he'
a[0:-1]
'hello worl'
a='hello world'
a[:2]
'he'
a[:3]
'hel'
a[:2:1]
'he'
a[:10:2]
'hlowr'
a[:5:3]
'hl'
a[:6:11]
'h'
a[6:11]
'world'
a[5:10]
' worl'
a[-5]
'w'
a[6:22222]
'world'
a[11:]
''
print'hello world'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#dlrow olleh
a[-1:-1]]
SyntaxError: unmatched ']'
a[-1::-1]
'dlrow olleh'
a[::=1]
SyntaxError: invalid syntax
a[::-1]
'dlrow olleh'
a
'hello world'
a[-8:-6]
'lo'
a='hwllo world'
a.capitalize()
'Hwllo world'
a
'hwllo world'
a=a.capitalize()
a
'Hwllo world'
a=title()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a=title()
NameError: name 'title' is not defined. Did you mean: 'tuple'?
a='hello world'
a.title()
'Hello World'
a.centre(50)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.centre(50)
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
a.center(50)
'                   hello world                    '
a,center(20)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a,center(20)
NameError: name 'center' is not defined
a.center(20)
'    hello world     '
a.center(40,'#')
'##############hello world###############'
a.count('l')
3
a.count('e')
1
a.1strip()
SyntaxError: invalid decimal literal
a.lstrip()
'hello world'
a.strip()
'hello world'
a.rstrip()
'hello world'
a.isupper()
False
a.islower()
True
a.isdown()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.isdown()
AttributeError: 'str' object has no attribute 'isdown'
a.upper()
'HELLO WORLD'
a.lower()
'hello world'
a.startswithit('he')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.startswithit('he')
AttributeError: 'str' object has no attribute 'startswithit'. Did you mean: 'startswith'?
a.startswith('he')
True
a
'hello world'
a.startswith('lo')
False
a.endswith('d')
True
len(a)
11
a[0]='M'
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a[0]='M'
TypeError: 'str' object does not support item assignment
dela[0]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    dela[0]
NameError: name 'dela' is not defined
b='gulnazakhter@gmail.com'
b.split('@')
['gulnazakhter', 'gmail.com']
b.split('akhter')
['gulnaz', '@gmail.com']
'@'.join(b)
'g@u@l@n@a@z@a@k@h@t@e@r@@@g@m@a@i@l@.@c@o@m'
b=b,split('@')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    b=b,split('@')
NameError: name 'split' is not defined
b=b.split('@')
b
['gulnazakhter', 'gmail.com']
'@'.join(b)
'gulnazakhter@gmail.com'
###############################################################
m=[12,'hi',2,3,500]
m[0]
12
m[1:3]
['hi', 2]
m[1:3:4]
['hi']
'hi',in m
SyntaxError: invalid syntax
'hi' in m
True
'hello' in m
False
'hi' not in m
False
2*m
[12, 'hi', 2, 3, 500, 12, 'hi', 2, 3, 500]
3*m
[12, 'hi', 2, 3, 500, 12, 'hi', 2, 3, 500, 12, 'hi', 2, 3, 500]
-1*m
[]
m+=['new value']
m
[12, 'hi', 2, 3, 500, 'new value']
m.append('abc')
m
[12, 'hi', 2, 3, 500, 'new value', 'abc']
m-=['hi']
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    m-=['hi']
TypeError: unsupported operand type(s) for -=: 'list' and 'list'
m.extend(['x','y','yes'])
m
[12, 'hi', 2, 3, 500, 'new value', 'abc', 'x', 'y', 'yes']
a.insert('hello',2)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.insert('hello',2)
AttributeError: 'str' object has no attribute 'insert'
m.(2,'hello')
SyntaxError: invalid syntax
m.insert(2,'hello')
m
[12, 'hi', 'hello', 2, 3, 500, 'new value', 'abc', 'x', 'y', 'yes']
m.pop(12)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    m.pop(12)
IndexError: pop index out of range
m.pop(0)
12
 mp=m.pop()
 
SyntaxError: unexpected indent
m.pop()
'yes'
m
['hi', 'hello', 2, 3, 500, 'new value', 'abc', 'x', 'y']
mp=m.pop()
m
['hi', 'hello', 2, 3, 500, 'new value', 'abc', 'x']
m.clear()
m
[]
n[12,34,45674,]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    n[12,34,45674,]
NameError: name 'n' is not defined
n=[112,34435543,2]
n.reverse()
n
[2, 34435543, 112]
n.sort()
n
[2, 112, 34435543]
max(n)
34435543
min(n)
2
m=[12,10,'hi','gulu']
m.index()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    m.index()
TypeError: index expected at least 1 argument, got 0
m.index('gulu')
3
m[1][0]
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    m[1][0]
TypeError: 'int' object is not subscriptable
m[[1][0]]
10
#############################################
t=45,67,'abc'
type(t)
<class 'tuple'>
len(t)
3
t[0]
45
t[:2]
(45, 67)
t[0]=45
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    t[0]=45
TypeError: 'tuple' object does not support item assignment
del t[1]
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    del t[1]
TypeError: 'tuple' object doesn't support item deletion
t
(45, 67, 'abc')
k=(12,59,(3,'hi',3.3),100)
type(t)
<class 'tuple'>
type(k)
<class 'tuple'>
k(3)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    k(3)
TypeError: 'tuple' object is not callable
k[3]
100
k[3][1]
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    k[3][1]
TypeError: 'int' object is not subscriptable
k[2]
(3, 'hi', 3.3)
k[2][1]
'hi'
k[2][1][1]
'i'
#########################################################
s= {1,1,2,3,4,4,3}
type(s)
<class 'set'>
print(s)
{1, 2, 3, 4}
s[0]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> s
{1, 2, 3, 4}
>>> s2=[]
>>> 
>>> s2={23,3,4,4}
>>> s.intersection(s2)
{3, 4}
>>> s.union(s2)
{1, 2, 3, 4, 23}
>>> s.add(100)
>>> s
{1, 2, 3, 100, 4}
>>> s.discard(1oo)
SyntaxError: invalid decimal literal
>>> s.discard(100)
>>> s
{1, 2, 3, 4}
>>> s.remove(3)
>>> s
{1, 2, 4}
>>> s1= {44,22,33}
>>> s.update(s1)
>>> s
{1, 2, 33, 4, 44, 22}
>>> s.clear()
>>> s
set()
