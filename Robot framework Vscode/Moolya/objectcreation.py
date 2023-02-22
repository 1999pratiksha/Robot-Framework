class my_class:
    global y,z
    y,z=10,20
    def add(self,a,b):
        y=a   #whatever value in a get it as y and a value 23
        z=b
        print(y+z)

obj = my_class()      #creation of object
obj.add(5,5)