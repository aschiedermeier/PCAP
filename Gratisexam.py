# Gratisexam
# 20 questions
# https://www.gratisexam.com/python-institute/pcap-exam/

print("\n#1: AC is True - a and b are the same list with different names")
a = [1]
b=a
a[0]=0

print(len(a)==len(b))
print(b[0]+1==a[0])
print(a[0]==b[0])
print(a[0]+1==b[0])

print("\n#2: CD is False. !!!Error in Exam!!! List b is a copy of list a, due to the colons")
a = [0]
b=a[:]
a[0]=1

print(len(a)==len(b))
print(b[0]+1==a[0])
print(a[0]==b[0])
print(a[0]+1==b[0])

print("\n#3: BC. Python strings can be concatenate and sliced. ")
word = "Word"
print(word+3*word[-1])

print("\n#4: BD. Tuples may be stored inside lists. Lists may be stored inside lists")
lst =[1,2,3]
tpl=(1,2,3)
lst1=[tpl,tpl]
tpl1=(lst,lst)
print(lst1)
print(tpl1)

print("\n#5: A. !!!Error in Exam!!! It's 3 chars shorter")
string = "012345"
print(string)
print (string[1:-2])
print (len(string)-len(string[1:-2]))

string = "0123456789"
print(string)
print (string[1:-2])
print (len(string)-len(string[1:-2]))

print("\n#6: C. Output is integer '2'")
lst =[1,2,3,4]
print(lst)
lst = lst [-3:2] # list with element "2"
print(lst)
lst=lst[-1] # integer "2"
print(lst)

print("""\n#7: C. Runtime exception, because: 
    1. 'int' object is not iterable.
    2 string 's' does not support item assignment""")
s="abc"
# for i in len(s):
#     s[i]=s[i].upper()
# print(s)

# fixed alternative
for i in range(len(s)):
    print(s[i].upper(),end="")

print("""\n#8: C,7. 
    list1 has 9 elements. 
    list2 goes backwards from last(-1) to one place before second (1)""")
list1=[False for i in range(1,10)]
print(list1)
list2 = list1[-1:1:-1]
print(list2)
print(len(list2))

print("""\n#9: A,D. !!!Error in Exam!!! 
    B: only works, if key in dict. Returns error, if key not in dict
    (Technically you can use it to check, if a runtime error is acceptable.)
    C: dict does not have method 'exists'""")
# 'key' in dict
dict = {'key':'value'}
print (dict)

print("key"in dict)
print (dict["key"])
#print(dict.exists("key"))
print("key" in dict.keys())

if "key"in dict:
    print("Key exists")

if dict["key"] != None:
    print("Key exists")

if "key" in dict.keys():
    print("Key exists")
    
# 'key' not in dict  
dict = {'keys':'value'}
print (dict)

print("key"in dict)
#print (dict["key"]) #error
#print (dict.exists("key")) #error
print("key" in dict.keys())

if "key"in dict:
    print("Key exists")

#if dict["key"] != None: # error
 #   print("Key exists") # error

if "key" in dict.keys():
    print("Key exists")

print("""\n#10: A,B. !!!Error in Exam!!! 
    C,D erroneous as Mom & Dad are non defined variables""")
dir={'Mom': 5551234567, 'Dad': 5557654321}
print(dir)
dir= {'Mom': '5551234567', 'Dad': '5557654321'}
print(dir)
#dir= {Mom: 5551234567, Dad: 5557654321}
print(dir)
#dir= {Mom: '5551234567', Dad: '5557654321'}
print(dir)

print("""\n#11: A not D !!!Error in Exam!!! 
    a module can be run like regualar code, as it is a script with funcitons and commands
    varible __name__ changes from __main__ to modulename, dependent from where to launch""")

print("""\n#12: B,D
    A: missing required pos arg 'a'
    C: non-keyword arg after keyword arg""")

def fun(a,b=0):
    return a*b
    
#print(fun(b=1))
print(fun(a=0))
#print(fun(b=1,0)) 
print(fun(1))

print("""\n#13: ABC
    """)

print("""\n#14: A: runtime exception, 2 errors in print line
    1. missing one bracket ]
    2. arguments for list and position argument mixed up, otherwise return '1' """)
def a (l,I):
    return l[I]

#print(a(0,[1))
print(a([1],0))

print("""\n#15: B
    hasattr() method to safely check, if class/object has a certain attribute""")

print("""\n#16: D
    first parameter of each method is """)

print("""\n#17: """)

print("""\n#18: """)

print("""\n#19: """)

print("""\n#20: """)