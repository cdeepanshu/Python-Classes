Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> names[]
SyntaxError: invalid syntax
>>> names=[]
>>> names
[]
>>> names['max','jon']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    names['max','jon']
TypeError: list indices must be integers or slices, not tuple
>>> names=['jon','max','sam']
>>> names
['jon', 'max', 'sam']
>>> names[0]
'jon'
>>> names[-1]
'sam'
>>> names.append('rohit')
>>> names
['jon', 'max', 'sam', 'rohit']
>>> age=[15,25,23,19]
>>> names.extend(age)
>>> names
['jon', 'max', 'sam', 'rohit', 15, 25, 23, 19]
>>> len(names)
8
>>> age
[15, 25, 23, 19]
>>> age[15:23]
[]
>>> age
[15, 25, 23, 19]
>>> age[0:3]
[15, 25, 23]
>>> age[-3: ]
[25, 23, 19]
>>> age[0:4:1]
[15, 25, 23, 19]
>>> age[0:4:2]
[15, 23]
>>> age[ :-1]
[15, 25, 23]
>>> age[-1: ]
[19]
>>> 
