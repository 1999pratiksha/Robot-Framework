list1=["moolya","python","classes","learn"]
for x in list1:
    for y in x:
        print(y)

s="prati"
for z in s:
    print(z)


list2=[["a","b","c"],["d","e"] ] #whatever there in list it will combine and print
for p in list2:
    for q in p:
        print(q)

list4=[['india','delhi'],['usa','new jersy'],['canada','vancouver']]
for b,c in list4: #it is used to comes in one line statement
    print("My country is "+b  + " and I lives in"+c)

list5=[["india","mumbai"],["bangalore","pune"]]
dict=dict(list5)
print(dict)
for x,z in dict:
    print(x,z)

list6=['india','delhi',"pune"]
set=set(list6) #typecast into sets
print(set)
#cant convert nested list in set
tuple=tuple(list6)
print(tuple)  #typecast into tuples
tuple2=tuple(list5)#but in tuple we convert nested list in tuple
print(tuple2)

