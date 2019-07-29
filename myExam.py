# questions i remember from my exam
# 29.7.2019
# passed with 87% :-)


print("""\n#1: True
    """)
print("John"<"Johnson")


print("""\n#2: slicing list for item returns list with one item, not item alone""")
a = [1,2,3,4]
b = a [1:2]
print(b)

print("""\n#3: 8""")
tup = (1,2)
tup = tup + 3*tup
print(len(tup))
print(tup)

print("""\n#4: if you test against several errors, use a bracket""")

try:
    x = 1/0
except (ZeroDivisionError, BaseException):
    print ("Error")


print("""\n#5: close() function
    •	the function expects exactly no arguments; the stream doesn't need to be opened
    •	the function returns nothing but raises IOError exception in case of error;
""")

print("""\n#6: method parameters
    There is one fundamental requirement - a method is obliged to have at least one parameter 
    (there are no such thing as parameterless methods - a method may be invoked without an argument, but not declared without parameters).
    The first (or only) parameter is usually named self. 
    We suggest that you follow the convention - it's commonly used, and you'll cause a few surprises by using other names for it.
    The name self suggests the parameter's purpose - it identifies the object for which the method is invoked.
""")

