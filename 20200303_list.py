a=[1,'a',5]

print(a)

a.append(4)

print(a[0:2])
print(len(a[0:2]))

b=f'this is {a}'
print(b)

a[0]='b'

print(a[-1])
x=[]

x.append(('a','f','g'))
print(x)



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



#e,f = thislist[1:2]
e= thislist

e.insert(0, "the")


e.append("asasda")


print(e)


e.remove("the")

e.pop()

del e[1]

e.clear()
print(e)


print(thislist)

j = ['amit','ankit','sanjay']

for k in j:
    print(k)

