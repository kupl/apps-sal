arr=[]
n=int(input())
for i in range(n):
    a=int(input())
    arr.append(a)
    arr.sort()
    p=arr.index(a)
    print((i-p)+1)
