#zip function using list
a=[1,2,3,4,5,6]
b=[100,200,300,400,500,600]
c=zip(a,b)     #pairing with a and b result in tuples
print(list(c))


#tupples using zip function
a=(10,20,30,40,50)
b=("ab","cd","ef","gt")
c=zip(a,b)
print(tuple(c))

#using for loops zip by above scenarios
for x,y in zip(a,b):
    print(x,y)

