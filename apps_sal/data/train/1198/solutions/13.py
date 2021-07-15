import math
n=int(input())
a=[int(i) for i in input().split()]
op={}
gcd={}
for i in a:
 gcd[i]=1
while(len(a)!=0):
 newa=[]
 x=a[0]
 for i in a[1:]:
  z=math.gcd(x,i)
  try:
   gcd[z]+=1
  except:
   gcd[z]=1
  newa.append(z)
  x=i
 a=newa
for i in gcd:
 j=i
 while(j<10**6+1):
  try:
   op[j]+=gcd[i]
  except:
   op[j]=gcd[i]
  j+=i
q=int(input())
for _ in range(q):
 try:
  print(op[int(input())])
 except:
  print(0)

