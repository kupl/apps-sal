# cook your dish here
for _ in range(int(input())):
 n=int(input())
 s=0
 if n%2==0:
  for i in range(2,n+1,2):
   s=s+(i*i)
 else:
  for i in range(1,n+1,2):
   s=s+(i*i)
 print(s)
