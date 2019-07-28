# Python Champion Test
# 40 questions, 65 mins
# passing score 70% (28)
# made 78% (31)
# https://github.com/srirambalasubramanian/Python-Champion/blob/b714eaed50c27342d35493a5865aee7006ba155d/Certification/PCAP%20Exam.ipynb

print("""\n#1: c pass
    most simple class """)
class X:
    pass

print("""\n#2: d - one parameter
    All class methods need to have at least the self parameter""")

print("""\n#3: a -[0,1,2,3]
    list was not changed by map and lambda""")
lst = [0,1,2,3]
map(lambda x : x+x,lst)
print(lst)

# changed code
print (map(lambda x : x+x,lst))
lst = [0,1,2,3]
for i in map(lambda x : x+x,lst):
    print(i)

print("""\n#4: a exception
    cannot order string and integer""")
try:
    "12">=12
except Exception as e:
    print (e)

print("""\n#5: a
    first line deletes list as a whole, second line just empties the list""")

lst1 = [0,1,2]
lst2 = [0,1,2]
del lst1    # first line
del lst2[:] # second line
try:
    print (lst1)
except Exception as e:
    print (e)

print (lst2)

print("""\n#6: c (and probably d)
    f is located in subpackage of c of subpackage of b of package a
    import a.b.c should be placed before that line""")

print("""\n#7: a,c
    Compiler is a program desinged to
    - translate source code into machine code 
    - execute the source code""")

print("""\n#8: d (more general), but should be b (exactly the same as ZeroDivisionError):
    We've defined our own exception, named MyZeroDivisionError, derived from the built-in ZeroDivisionError. 
    As you can see, we've decided not to add any new components to the class. 
    In effect, an exception of this class can be - depending on the desired point of view - 
    treated like a plain ZeroDivisionError, or considered separately.""")

class MyZeroDivisionError(ZeroDivisionError):
    pass

print("""\n#9: 1""")
i = 0
while i !=0:
    i = i-1
else:
    i= i +1 
print(i)

print("""\n#10: 3""")
def x():
    return 2
x = 1 + x()
print(x)

print("""\n#11: BC
    B & C inherit a from A but alter it
    they inherit b without change
    do calls (unaltered) b which calls (altered) a
    B().do() is a method to call a method without an object
    """)
class A:
    def a (self):
        print("A",end ="")
    def b(self):
        self.a()
class B(A):
    def a (self):
        print("B",end="")
    def do(self):
        self.b()
class C(A):
    def a (self):
        print("C",end="")
    def do(self):
        self.b()


B().do()
C().do()

print("""\n#12: a,not c (error in test)
    list comprehension does not work with equal sign""")
lst = [x ** 3 for x in range(5)]
print (lst)
try:
    eval("[ x = i* i* i for i in range(5) ]")
except Exception as e:
    print (e)


print("""\n#13: 2 1
    actually 21, as no space in beween""")
def f(a):
    for i in reversed(a):
        yield i + 1
for i in f([x for x in range(2)]):
    print(i,end='')

print("""\n#14: dict.keys()""")

print("""\n#15: a,b error in test
    the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; 
    if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains untouched.)""")

print("""\n#16: The class component’s name will be mangled""")
class A:
    def __a(self):
        print("A")
try:
    A().__a()
except Exception as e:
    print (e)

A()._A__a()

print("""\n#17: tuple, not regular varibale. error in test.""")
ent = 1,2,4,8
print(type(ent))

print("""\n#18:  b,c
    technically the program does not stop, if you catch the error.
    • you may want to put it into your code where you want to be absolutely safe from evidently wrong data, 
    and where you aren't absolutely sure that the data has been carefully examined before (e.g., inside a function used by someone else)
• It evaluates the expression;
• if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different than None, it won't do anything else;
• otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say that the assertion has failed)""")

a = 5
try: 
    assert (a == 4)
except AssertionError:
    print("AssertionError")


print("""\n#19: 2 identical non-empty lines""")
try:
    raise Exception("Personalized error message!")
except Exception as e:
    print(e)
    print(e.__str__())

print("""\n#20: 3
    data[0]+3 = 1+3=4
    index method searches position of value "4" in list --> 3 """)
data = [1,2,3,4,5,6]
idx = data.index(data[0]+3)
print (idx)

print("""\n#21: exception
    actually 2 errors""")
try:
    s = "abc"
    for i in len(s):
        s[i]=s[i].upper()
    print(s)
except Exception as e:
    print (e)

try:
    s = "abc"
    s[0]=s[0].upper()
except Exception as e:
    print (e)
    

print("""\n#22: runtime exception""")
try:
    strng = "abcdef"
    def fun(s):
        del s[2]
        return s
    print(fun(strng))
except Exception as e:
    print (e)

print("""\n#23: 1 2""")
def f(n):
    for i in range(1,n+1):
        yield i
for i in f(2):
    print(i,end="")

print("""\n#24: a,c
    __module__: function for name of module with class definition
    __bases__: filled with superclasses, not subclasses
    __name__: name of class, only inside classes""")

print("""\n#25: 1""")
def fun(x):
    return x if x%2 !=0 else 2
print(fun(fun(1)))

print("""\n#26: b,d
    interpreter executes source code on the fly
    translates the source code into machine code
    debugger is a tool to check the source code in order to see if it's correct""")

print("""\n#27: 3.0""")
print(3//2+6/3)

print("""\n#28: b,d""")
a = [1]
b=a
a[0]=0

print(a[0]==b[0])
print(len(a)==len(b))

print("""\n#29: b,d""")
x=1
print(chr(x))
print(ord(chr(x))==x)
x="1"
print(ord(x))
print(chr(ord(x))==x)

print("""\n#30: 15, not 3, error in test""")
val = 15
val+=1
val/=1
print(val)

print("""\n#31: 21
    val: 12,14,21
    both if branches, but no else branch""")
val = 12
if val%2==0:
    val+=2
if val % 7 ==0:
    val+=val//2
else:
    val-=val//2
print(val)

print("""\n#32: 2""")
number = 1
text = """
number = number +1 
"""
number *=2
print(number)

print("""\n#33: error""")

try:
    y = "abc"
    def x():
        print(y,end='')
        y = "cba"
    print(x())
except Exception as e:
    print(e)

# alternative code without local variable works
    y = "abc"
    def x():
        print(y,end='')
    print(x())
print("""\n#34: c""")
print("line",end="")

print("""\n#35: 1
    i gets reduced alternating between  while and else branch until it reaches 1 and while block breaks""")
i = 5
while i > 1:
    while i % 2 !=0:
        i-=1
    else:
        i-=1
print (i)

print("""\n#36: d,not c - error in test
    mixed up capitalize() and title()""")
s = "DON’T JUDGE A BOOK BY ITS COVER"
print(s.capitalize())
print(s.title())
print(s.upper())

print("""\n#37: 256""")
def fun(a,b=0,c=5,d=1):
    return a ** b ** c
print(fun(b=2,a=2,c=3))

print("""\n#38: python, as for loop does not affect s""")
s = "python"
for i in range(len(s)):
    i=s[i].upper()
print(s,end="")

print("""\n#39: 125""")
i = 250
while len(str(i))>72:
    i*=2
else:
    i//=2
print(i)

print("""\n#40: 512""")
print (2**3**2**1)