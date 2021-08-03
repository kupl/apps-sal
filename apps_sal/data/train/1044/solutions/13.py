n = int(input())
mylist = []
while(n > 0):
    num = int(input())
    sum = 0
    while(num > 0):
        rem = num % 10
        sum += rem
        num = num // 10
    mylist.append(sum)
    n = n - 1
for i in mylist:
    print(i)
