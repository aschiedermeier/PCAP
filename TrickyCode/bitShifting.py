# bitshifting
# >> 1 equals modulo 2
# << equals times 2
# using lambda function to create bishift function that 

# bitshifting
var = 5
varRight = var >> 1
varLeft = var << 1
print(varLeft)
print(varRight)

# bitshifting by 1 equals multiplying and modulo 2 
print(var*2)
print (var//2)

# compare values to show equality
for i in range (10):
    print (i,end=" ")
    print (i << 1,end=" ")
    print (i * 2)
    
for i in range (10):
    print (i,end=" ")
    print (i >> 1,end=" ")
    print (i // 2)

# using lambda function to build functions with various multiplicators

# lambda in function
def myfunc1 (n):
    return lambda a: a * (2**n)
def myfunc2 (n):
    return lambda a: a << n

# make new functions: n defines the shift length
n = 2
myMultiplyer = myfunc1(n)
myLeftShift = myfunc2(n)

# print values to show equality
for i in range (10):
    print (i,end=" ")
    print (myMultiplyer(i),end=" ")
    print (myLeftShift(i))
print(9<<2)

# same for right shift and modulo

def myfunc1 (n):
    return lambda a: a // (2**n)
def myfunc2 (n):
    return lambda a: a >> n

n=2
myModulo = myfunc1(n)
myRightShift = myfunc2(n)

for i in range (10):
    print (i,end=" ")
    print (myModulo(i),end=" ")
    print (myRightShift(i))


print(9>>2)

