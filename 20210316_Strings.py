# this is multiline
a = """sdakjfsakfsa
dsafhjbskfasnsada
safdknfsaasnlsakmcqmas"""

print(type(a[12]))
print(a[13])
#
# for a in a:
#     print(a)

b = 'This is string testing'

print(b[0:3])
print(b.split(' '))
print(b.upper().replace(b.upper() ,"testing"))

age = 36
txt = "My name is John, I am " + str(age)
print(txt)


age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {0} pieces of item {2} for {1} dollars."
print(myorder.format(quantity, itemno, price))



text = 'hi this\'s is ayush'
print(text)


txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)





#print('This' not in b)
