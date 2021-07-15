# cook your dish here
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
s=0
i=0
while(k>=0 and i<len(a)):
 if k-a[i]>=0:
  k=k-a[i]
  s+=1
  i+=1
 else:
  i+=1
print(s)
