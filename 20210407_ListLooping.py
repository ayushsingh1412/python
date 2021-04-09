a=[1,2,'saa',4545,'asd']

b= ['cat','dog','elephant','tiger','zebra']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

c=[]

for x in b:
    if 'a' in x:
        print(x)
        c.append(x)

print(c)

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist.sort(reverse= True)
print(thislist)

print("b")



def mySort(n):
    return abs(n-50)

