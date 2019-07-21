# Free Sample Test
# From official website
# 40 questions
# 65 mins
# 28 to pass
# made 29 in 1st attempt
# https://pythoninstitute.org/certification/download/566/

print("""\n#1: from right to left. 2**9 = 512""")

print("""\n#2: usage of \\, \" and \' """)

print("""\n#3: lenght of string(i) is 3, so we go else-path. """)

print("""\n#4: end-argument replaces new line break""")

print("""\n#5: Bool""")

print("""\n#6: XOR""")

print("""\n#7: two correct answers - select ALL that apply""")

print("""\n#8: b = 1 --> c = 2 """)

print("""\n#9: A: 3 stars. 
    No error, the else is ok. 3.1.2.16
    The while and for loops can also have an else clause in Python. 
    The else clause executes after the loop finishes its execution as long as it has not been terminated by break""")

print("""\n#10: all have only one line, as end command deletes the break line command.""")
for i in range (1,4,2):
    print("*",end="*")
print("**")

print("""\n#11: D: The Python Language Reference is the official reference manual that
describes the syntax and semantics of the Python language.
G: Lists and strings in Python can be sliced.
""")

print("""\n#12: False, as the code point of 20 is smaller than of 30.
    Careful: codepoint 8 is higher than 30""")
x= "20"
y= "30"
print(x>y)
print (chr)
x= "8"
y= "30"
print(x>y)

print("""\n#13: A, ifend  slice goes beyond the range of strings no problem(error).
    Whole string gets printed""")

print("""\n#14: deleted first 3 items""")

print("""\n#15: A - for item in dict: print item - returns only key. 4.1.6.11
    variant C: for item in dict.items()""")
dict = { 'a': 1, 'b': 2, 'c': 3 }
for item in dict:
    print(item)

# alternative code
for value in dict.values():
    print(value)

for key,value in dict.items():
    print(key+": "+str(value))

print("""\n#16: what happens in for loop stays in for loop
    unless it gets printed out or returned""")
s = 'python'
for i in range(len(s)):
    i = s[i].upper()

print(s, end="")

# alternative code
s = 'python'
for i in range(len(s)):
    i = s[i].upper()
    print(i)
print(s, end="")

print("""\n#17: E erroneous, as can't divide by zero also valid for floor division""")
# lst = [i // i for i in range(0,4)]
lst = [i // i for i in range(1,4)]
sum = 0
for n in lst:
 sum += n
print(sum)


print("""\n#18: C: 3 stars - nested list comprehension 3.1.7.2
    second parts scans nested list for values below 2
    """)

lst = [[c for c in range (r)]for r in range(3)]
print (lst)

# recreated list with nested for loop
lst=[]        
for r in range(3):
    sublst=[]
    for c in range (r):
        sublst.append(c)
    lst.append(sublst)
print (lst)   

for x in lst:
    for y in x:
        if y < 2:
            print('*',end='')

print("""\n#19: C, last item of list. no need to calcualate that 2**10 is 1024.""")
lst = [2 ** x for x in range(0, 11)]
print(lst[-1])

print("""\n#20: lst1 is a string with lenght 5
    lst2 is a list with length 2.
    we compare apples and pears by the kg, so it's ok""")

lst1 = "12,34"
print (lst1)
print(type(lst1))
print(len(lst1))

lst2=lst1.split(',')
print(lst2)
print(type(lst2))
print(len(lst2))

print(len(lst1)<len(lst2))

print("""\n#21: right to left order. 2 to the power of 8 is 256
    keyword arguments were also ok. 
    no problem that d was not used.
    that's what she said...""")
def fun(a, b=0, c=5, d=1):
 return a ** b ** c
print(fun(b=2, a=2, c=3))

print("""\n#22: lambda always returns 3, x is not used. but need to set x as argument, as it's needed""")
x = 5
f = lambda x: 1 + 2
print(f(x))

# alternative code without x
x = 5
f = lambda : 1 + 2
print(f())

print("""\n#23: making alias for the variable pi makes the original name inaccessible""")
from math import pi as xyz # line 01
#print(pi) # line 02
# correct code
print(xyz)

print("""\n#24: """)

print("""\n#25: """)

print("""\n#26: """)

print("""\n#27: G - error due to missing positional argument - 
    Exception gets raised in line G, where the program prints and calls the function.
""")

# Traceback (most recent call last):
# File "C:\Users\Andi\Documents\GitHub\PCAP\FreeSampleTest.py", line 168, in <module>
# print(x(a)) # line 5
# TypeError: x() missing 1 required positional argument: 'b' 

# a = 'hello' # line 1
# def x(a,b): # line 2
#  z = a[0] # line 3
#  return z # line 4
# #print(x(a)) # line 5

print("""\n#28: """)

print("""\n#29: """)

print("""\n#30: """)
def gen():
    lst = range(5)
    for i in lst:
        yield i*i
for i in gen():
    print(i, end="")

print("""\n#31: ACD
    B:Some objects contain references to other objects; these are called containers. 
    Examples of containers are tuples, lists and dictionaries. The references are part of a container’s value.
    E: There is no object variables in Python, only instance variables.
    """)

print("""\n#32: ACD
    B: issubclass(class1, class2) is an example of a function that returns
        True if class2 is a subclass of class1 
        --> wrong order: True if class1 is subcalss of class2
""")

print("""\n#33: CD
    A. A class definition may have any number of constructors, but their
        names must be unique
        --> wrong: a class can have zero or no constructor.
    B. It is not possible to safely check if an object has a certain attribute
        --> wrong: hasattr() does that
    C. A class constructor cannot return a value
        --> correct: 6.1.4.3
    D. __bases__ is a tuple filled with the names of all the direct superclasses
        --> correct: 6.1.4.8
    E: issubclass(c1, c2) is a function that checks if c1 is an object
        derived from class c2
        --> wrong: isinstance () does that
    """)

print("""\n#34: C
    ZeroDivisionErrors also for modulo.
    exception gets raised in line of division, not in print line 
    (different to function, which needs to be called first)""")
# Example 1
x = 1
y = 0
#z = x%y
#print(z)
# Example 2
x = 1
y = 0
#z = x/y
#print(z)

print("""\n#35: D
    exception gets raised, except branch prints, finally branch always gets excuted.""")
x = 0
try:
    print(x)
    print(1 / x)
except ZeroDivisionError:
    print("ERROR MESSAGE")
finally:
    print(x + 1)
print(x + 2)

print("""\n#36: B
    polymorphism: B overwrites the a method
    C defines new method b
    extra: C also inherits the polymorphed method a from B --> prints B.""")
class A:
    def a(self):
        print("A", end='')

class B(A):
    def a(self):
        print("B", end='')
class C(B):
    def b(self):
        print("B", end='')

a = A()
b = B()
c = C()
a.a()
b.a()
c.b()
## extra code
print()
c.a()

print("""\n#37: D: print Hello, then empty line. as pure Exception does not print out error name
    alternative code:
    ZeroDivisionError gets raised and printed""")
try:
    print("Hello")
    raise Exception
    print(1/0)
except Exception as e:
    print(e)
## alternative code
try:
    print("Hello")
    print(1/0)
except Exception as e:
    print(e)
print("""\n#38: D
    example 1: upper error gets raised and prints standard message A, line below does not get executed at all
    example 2: error with custom message gets raised and prints it.
    """)
# Example 1
class CriticalError(Exception):
    def __init__(self, message='ERROR MESSAGE A'):
        Exception.__init__(self, message)
#raise CriticalError
#raise CriticalError("ERROR MESSAGE B")
# Example 2
class CriticalError(Exception):
    def __init__(self, message='ERROR MESSAGE A'):
        Exception.__init__(self, message)
#raise CriticalError("ERROR MESSAGE B")

print("""\n#39: ADF
    correct methods (not functions) to access the file
    A. print(file.readlines())
    D. for l in file:
        print(l)
    F. print(file.read())
""")

print("""\n#40: ABD
    open('file','w') 
    - either opens existing file and deletes all file content or
    - creates new file.
    A. open the file file.txt in write mode
    B. delete the file contents if the file file.txt already exists
    D. create the file file.txt if it does not exist
""")
