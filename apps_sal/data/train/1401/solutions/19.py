# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
c,s=0,0
for i in a:
 s+=i
 if s<=k:
  c+=1
print(c)
