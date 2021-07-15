n=int(input())
a=list(input())
arr=[]
counter=a.count('n')
counter2=a.count('r')
for i in range(counter):
    arr.append(1)
for i in range(counter2):
    arr.append(0)
print(*arr)

