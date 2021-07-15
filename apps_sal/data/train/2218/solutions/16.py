R=lambda:map(int,input().split())
n=int(input())
a=*zip([1]*n,range(1,n+1),R()),*([*R()]for _ in[0]*int(input()))
r=[-1]*n
m=0
for t,p,*x in a[::-1]:
 if t>1:m=max(m,p)
 elif r[p-1]<0:r[p-1]=max(x[0],m)
print(*r)
