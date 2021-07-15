def gcd(a,b):
 if a==0:
  return b
 return(gcd(b%a,a))
def lcm(a,b):
 return((a*b)/gcd(a,b))
T=int(input())
for _ in range(0,T):
 N=int(input())
 l=[]
 A=list(map(int,input().split()))
 for i in range(0,len(A)-1):
  l.append(A[i]-A[i+1])
 print(min(l))

