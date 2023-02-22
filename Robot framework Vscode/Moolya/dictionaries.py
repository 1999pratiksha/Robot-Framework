#dictionary to store the multiple url or values
   #key         value
a={"url1":"google.com","url2":"amazon.com"}
b={1:"pratiksha",2:"naik"}
print(b[1])
print(a["url1"])
b[3]="bandekar"#we can add the value in b dictionary
print(b)
print(b[3])
print(b.get(1))#in first index prashant is there it will display
print(b.keys())#how many keys are there it will display
print(b.items())#results comes in the form of tuples
#print(b.pop())
print(b.popitem())#it will remove the last item
print(b.keys())
b.update({3:"demoqa.com",4:"orangehrm"})#here updating values with method
print(b)

