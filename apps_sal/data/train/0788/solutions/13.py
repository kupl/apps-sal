n = int(input())
mylist = []
while n > 0:
    num = input()
    first = num[0]
    last = num[-1]
    first = int(first)
    last = int(last)
    sum = first + last
    mylist.append(sum)
    sum = 0
    n = n - 1
for i in mylist:
    print(i)
