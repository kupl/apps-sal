n,m,k=map(int,input().split())
a=0
for i in range(n):
 t=list(map(int,input().split()))
 q=t[-1]
 t.pop(-1)
 if q<=10 and sum(t)>=m:
  a+=1
print(a)
