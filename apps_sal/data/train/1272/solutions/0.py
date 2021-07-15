# cook your dish here
n=int(input())
for _ in range(n):
 a=int(input())
 if(a%2==0):
  f=(a//2)-1
  s=a-f
 else:
  f=(a//2)
  s=a-f
 print(f,s)
