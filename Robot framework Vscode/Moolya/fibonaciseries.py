'''def fibonacci(n):
    a,b=0,1
    while a<=n:
        print(a)
        a,b= b,a+b
fibonacci(50)'''

'''#using for loop
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(10)'''
import math
def square(x):
    t=int(math.sqrt(x))
    return t*t==x

def isFibonacci(n):
    return square(5*n*n + 4) or square(5*n*n - 4)

for j in range(1,31):
     if (isFibonacci(j) == True):
        print (j,"is a Fibonacci Number")
     else:
         print (j,"is a not Fibonacci Number ")


