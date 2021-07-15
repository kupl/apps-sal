# cook your dish here
for _ in range(int(input())):
 l,b=map(int,input().split())
 for i in range(1,min(l,b)+1):
  if l%i==0 and b%i==0:
   s=(l*b)//i**2
 print(s)
