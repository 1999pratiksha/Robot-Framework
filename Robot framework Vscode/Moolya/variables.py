'''x=20
def add(a,b):
    print(x)
    print(a+b)

def sub(a,b):
    print(a-b)
    print(x)'''


x=10
def multiply():       #inside one method only child method is created we can access the values from both child and parent without global variable
    x=20              #local variable is con
    print(x)
    def sub():
        x=30
        print(x)
        def add():
          
            print(x)
        add()
    sub()
multiply()