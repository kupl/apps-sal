def gcd(a,b):
 if b==0:
  return a
 else:
  return gcd(b,a%b)
 
def main():
 t=int(input())
 while t!=0:
  t=t-1
  n=int(input())
  if n==1:
   print(input())
  else:
   a=list(map(int,input().split(" ")))
   p=a[0]
   for i in range(1,n):
    p=gcd(p,a[i])
    if p==1:
     break
   print(n*p)
def __starting_point():
 main()
  
  

__starting_point()
