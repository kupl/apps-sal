
r,c,n=list(map(int,input().split()))
ro=[0]*n
co=[0]*n
for i in range(n):
    a,b=list(map(int,input().split()))
    ro[a]+=1
    co[b]+=1
ma=0
ma+=max(ro)
ma+=max(co)
print(ma)







