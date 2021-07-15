# cook your dish here
def gcd(a,b):
 if b==0:
  return a
 else:
  return gcd(b,a%b)
  
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 a=l[0]
 for i in range(1,n):
  a=gcd(a,l[i])
 if a==1:
  print(n)
 else:
  print(-1)
  

