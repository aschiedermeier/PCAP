# Python Champion Test
# 40 questions, 65 mins
# passing score 70% (28)
# 
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

print("""\n#8: """)

print("""\n#9: """)

print("""\n#10: """)

print("""\n#11: """)

print("""\n#12: """)

print("""\n#13: """)

print("""\n#14: """)

print("""\n#15: """)

print("""\n#16: """)

print("""\n#17: """)

print("""\n#18: """)

print("""\n#19: """)

print("""\n#20: """)

print("""\n#21: """)

print("""\n#22: """)

print("""\n#23: """)

print("""\n#24: """)

print("""\n#25: """)

print("""\n#26: """)

print("""\n#27: """)

print("""\n#28: """)

print("""\n#29: """)

print("""\n#30: """)

print("""\n#31: """)

print("""\n#32: """)

print("""\n#33: """)

print("""\n#34: """)

print("""\n#35: """)

print("""\n#36: """)

print("""\n#37: """)

print("""\n#38: """)

print("""\n#39: """)

print("""\n#40: """)