x = 'awesome'

i = input("enter the no of iteration")

def myFunc(i):
    while int(i)>0:
        x='Fantastic'
        print(x)
        i= i-1
        print(i)
myFunc(int(i))
print(i)
print(x)