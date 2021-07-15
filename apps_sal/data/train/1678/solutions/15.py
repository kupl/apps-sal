# cook your dish here
n,m=map(int,input().split())
l=list(map(int,input().split()))
d=list(map(int,input().split()))
x=l.index(min(l))
y=d.index(max(d))
for i in range(n):
    if(i==x):
        for j in range(m):
            print(i,j)
    else:
        print(i,y)

