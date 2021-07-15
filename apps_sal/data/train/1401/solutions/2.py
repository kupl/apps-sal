# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
s=0
c=0
for i in range(n):
 if s+a[i]<=k:
  s+=a[i]
  c+=1
 else: break
print(c)
