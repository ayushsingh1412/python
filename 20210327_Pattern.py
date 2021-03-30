a = '#'

i = 0
while i <= 3:
    j = 0
    while j <= 3:
        print(a, end='')
        j += 1
    print()
    i += 1

for i in range(5):
    for j in range(5-i):
        print(a, end='')
    print()


x= range(5)
print(x)
