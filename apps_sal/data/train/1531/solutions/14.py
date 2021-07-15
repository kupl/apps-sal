# cook your dish here
n=int(input())
l=list(map(int,input().split()))
q=int(input())
for u in range(q):
    x,y=list(map(int,input().split()))
    x-=1
    if(x-1>=0):
        l[x-1]+=(y-1)
    if(x+1<n):
        l[x+1]+=(l[x]-y)
    l[x]=0
for i in l:
    print(i)

