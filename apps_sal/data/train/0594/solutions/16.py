n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
maxi=a[0]
p=0
for i in range (n):
 sumi=a[i]
 if (sumi>maxi):
  maxi=sumi 
  
 for j in range (i+1,n):
  sumi+=a[j]
  if (i==0):
   p+=a[j]
  if (sumi>maxi):
   maxi=sumi
  
 if (sumi>maxi):
  maxi=sumi 
  
p+=a[0]

print(p-maxi+maxi/x)

