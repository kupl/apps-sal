# cook your dish here
n=int(input())
a=[int(X) for X in input().split()]
a=[0]+a
for j in range(int(input())):
    x,y = map(int,input().split())

    if x!=1:
        a[x-1]+=y-1
    if x!=n:
        a[x+1]+=(a[x]-y)
    a[x]=0
print(*a[1:],sep='\n')
