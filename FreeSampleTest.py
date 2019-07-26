# Free Sample Test
# From official website
# 40 questions
# 65 mins
# 28 to pass
# made 29 in 1st attempt
# https://pythoninstitute.org/certification/download/566/

print("""\n#1: from right to left. 2**9 = 512""")

print("""\n#2: usage of \\, \" and \' """)
a=b=c=d = None

a="Peter's sister's name's \"Anna\""
b='Peter\'s sister\'s name\'s \"Anna\"'
#c= "Peter's sister's name's "Anna""
#d= 'Peter's sister's name's "Anna"'

print (a)
print (b)
print (c)
print (d)

print("""\n#3: lenght of string(i) is 3, so we go else-path. """)

print("""\n#4: end-argument replaces new line break""")

print("""\n#5: Bool""")

print("""\n#6: XOR""")

print("""\n#7: two correct answers - select ALL that apply""")

print("""\n#8: b = 1 --> c = 2 """)

print("""\n#9: A: 3 stars. 
    No error, the else is ok. 3.1.2.16
    The while and for loops can also have an else clause in Python. 
    The else clause executes after the loop finishes its execution as long as it has not been terminated by break
    In this case: 3 starts in while loop, then break, so no else path""")

i = 10
while i > 0 :
    i -= 3
    print("*")
    if i <= 3:
        break
else:
    print("*")

print("""\n#10: ex1: no end --> break line command
		ex 2-4 have only one line, as end command deletes the break line command.""")
# Example 1
for i in range(1, 4, 2):
    print("*")
print()

# Example 2
for i in range(1, 4, 2):
    print("*", end="")
print()

# Example 3
for i in range(1, 4, 2):
    print("*", end="**")

print()

# Example 4
for i in range(1, 4, 2):
    print("*", end="**")
print("***")


print("""\n#11: 
A: Unicode assigns unique (unambiguous) characters (letters, hyphens, ideograms, etc.) to more than a million code points. 
The first 128 Unicode code points are identical to ASCII, 
and the first 256 Unicode code points are identical to the ISO/IEC 8859-1 code page (a code page designed for western European languages).

B: One of the most commonly used is UTF-8.
The name is derived from Unicode Transformation Format.
The concept is very smart. UTF-8 uses as many bits for each of the code points as it really needs to represent them.

C: The system named ASCII (short for American Standard Code for Information Interchange) is the most widely used, 
and you can assume that nearly all modern devices (like computers, printers, mobile phones, tablets, etc.) use that code.
The code provides space for 256 different characters, but we are interested only in the first 128. 

D: The Python Language Reference is the official reference manual that
describes the syntax and semantics of the Python language.

E,F:First of all, Python's strings (or simply strings, as we're not going to discuss any other language's strings) are immutable sequences.
Strings aren't lists, but you can treat them like lists in many particular cases.
Moreover, everything you know about slices is still usable.

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

print("""\n#13: A, if end  slice goes beyond the range of strings no problem (no error).
    Whole string gets printed.
    If i print the single items on the borders, i get error message.""")
s = "Hello, Python!"

print(s[-14:15])
# print(s[-15]) #error
print(s[-14])
print(s[13])
#print(s[14]) # error
print(s[-15:16]) # no error
print("""\n#14: deleted first 3 items""")

print("""\n#15: A - for item in dict: print item - returns only key. 4.1.6.11
    variant C: for item in dict.items()""")
dict = { 'a': 1, 'b': 2, 'c': 3 }
for item in dict:
    print(item)

# ame result
for key in dict.keys():
    print(key)

# alternative code
for value in dict.values():
    print(value)

for key,value in dict.items():
    print(key+": "+str(value))
    
# also working, but ugly
for item  in dict.items():
    print(item)

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

print("""\n#19: C, last item of list. no need to calcualate that 2**10 is 1024.
(But i should know those numbers by now anyway)""")
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

print("""\n#24: BC
The content of the __init__.py file is executed when any of the package's modules is imported. 
If you don't want any special initializations, you can leave the file empty, but you mustn't omit it.

B. It can execute an initialization code for a package
C. It is required to make Python treat a given directory as a Python
package directory
""")


print("""\n#25: F, i need to call the function, not the module. If corrected, then Answer A""")
#corrected code
from random import randint
for i in range(10):
 print(randint(1, 5))

import random 
for i in range(10):
 print(random.randint(1, 5))
 
from random import randint as ra
for i in range(10):
 print(ra(1, 5))

print("""\n#26: A: 8""")
x = 1 # line 1
def a(x): # line 2
    return 2 * x # line 3
x = 2 + a(x) # line 4
print(a(x)) # line 5


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

print("""\n#28: D""")
s = 'SPAM'
def f(x):
    return s + 'MAPS'
print(f(s))


print("""\n#29: BD
A. Positional arguments are also called keyword arguments
B. The order of arguments matters when they are passed positionally
C. The order of arguments matters when they are passed by their name
D. A function can be called with a mix of positional and keyword arguments
""")

print("""\n#30: B""")
def gen():
    lst = range(5)
    for i in lst:
        yield i*i
for i in gen():
    print(i, end="")

print("""\n#31: ACD
    B:Some objects contain references to other objects; these are called containers. 
    Examples of containers are tuples, lists and dictionaries. The references are part of a container’s value.
    D: A constructor is used to instantiate an object.
    The act of creating an object of the selected class is also called an instantiation 
    (as the object becomes an instance of the class).
    Can be made also from simple class without constructor.
    So: A constructor is not necessarily needed to instantiate an object, but  statement D is still true.
    E: There is no object variables in Python, only instance variables.
    """)

print("""\n#32: ACD
    B: issubclass(class1, class2) is an example of a function that returns
        True if class2 is a subclass of class1 
        --> wrong order: True if class1 is subcalss of class2
    D: The situation in which the subclass is able to modify its superclass behavior 
    (just like in the example) is called polymorphism. 
    polymorphism helps the developer to keep the code clean and consistent.
    Polymorphism is a fancy word that just means the same function is defined on objects of different types.
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

print("""\n#37: D: prints "Hello", then empty line. as pure risen Exception does not print out error name.
    alternative code:
    ZeroDivisionError gets raised due to 1/0 and it's name gets printed""")
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
    A. print(file.readlines()) # prints line as a list
    B. wrong: readlines is not a function but a method
    C: wrong:print(file.readlines(:) 1. bracket missing. 2. can't splice here
    D. for l in file: # writes line by line, but with one empty line in between
        print(l)
    E. wrong: print(file.lines()) - no attribute lines
    F. print(file.read()) # writes line by line, like in text, perfect method
    G. wrong: print(read.file(test.txt)) - no item read, no method file

""")
# i need to open the file for every print command.
# otherwise nothing to print.
# it's enough to close it only once at the end.
file = open("test.txt")
print(file.readlines())

file = open("test.txt")
for l in file:
    print(l)

file = open("test.txt")
print(file.read())

file.close()

print("""\n#40: ABD
    open('file','w') 
    - Opens existing file and deletes all file content.
    - If file does not exist, it creates new file.
    A. open the file file.txt in write mode
    B. delete the file contents if the file file.txt already exists
    D. create the file file.txt if it does not exist
""")
f = open("file.txt", "w")
f.close()
