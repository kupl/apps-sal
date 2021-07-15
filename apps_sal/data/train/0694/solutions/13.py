t=int(input())
n=[]
l=[]

def gcd(a,b): 
 if(b==0): 
  return a 
 else: 
  return gcd(b,a%b)

for i in range(t):
 n.append(24*int(input()))
 k=input().split()
 l.append(k)

for i in range(t):
 a=l[i]
 a= [int(k) for k in a]
 a[0]=(a[0]*a[1])//gcd(a[0],a[1])
 a[0]=(a[0]*a[2])//gcd(a[0],a[2])

 j=a[0]
 print(n[i]//j)

