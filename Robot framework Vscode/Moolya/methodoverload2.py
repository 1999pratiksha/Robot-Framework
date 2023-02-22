#one parameter-square of a no
#two parameter-add
#three parameter-multiply
#four parameter-find perfect square

from multipledispatch import dispatch
import math
@dispatch(int)
def cal(x):
    print(x**2)
@dispatch(int,int)
def cal(x,y):
    print(x+y)
@dispatch(int,int,int)   
def cal(x,y,z):
     print(x*y*z)
@dispatch(int,int,int,int)
def cal(x,y,z,a):
    sq=x*y*z*a
    k= int(math.sqrt(sq))
   
    if k**2==sq:
        print("this is perfect square:",sq )
    else:
        print("this is not a perfect square",sq)

cal(1,3,3,3)   
cal(5,2,4)
cal(5,5)
cal(4)






