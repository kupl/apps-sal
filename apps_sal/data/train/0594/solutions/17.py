n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
mini,maxi=a[0],a[0]
p=0
for i in range (n):
 sumi=a[i]
 if (sumi>maxi):
  maxi=sumi 
 if (sumi<mini):
  mini=sumi 
 for j in range (i+1,n):
  sumi+=a[j]
  if (i==0):
   p+=a[j]
  if (sumi>maxi):
   maxi=sumi
  if (sumi<mini):
   mini=sumi
 if (sumi>maxi):
  maxi=sumi 
 if (sumi<mini):
  mini=sumi 
p+=a[0]

print(min((p-maxi+maxi/x),(p-mini+mini/x)))

