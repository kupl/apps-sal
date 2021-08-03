n = int(input())
mylist = []
while n > 0:
    b = int(input())
    mylist.append(b)
    n = n - 1
print()
mylist.sort()
for i in mylist:
    print(i)
