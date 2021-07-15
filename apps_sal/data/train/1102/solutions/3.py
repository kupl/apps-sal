# cook your dish here

n=int(input())
for i in range(n):
 num=int(input())
 a=[]
 while num:
  a.append(num%10)
  num//=10
 mul=1
 for j in a:
  if j==7 or j==9:
   mul*=4
  elif j!=0 and j!=1:
   mul*=3
 print(mul%1000000007)

