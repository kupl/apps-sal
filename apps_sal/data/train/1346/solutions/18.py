# Hello World program in Pytho
# cook your dish here
for i in range(int(input())):
 n,w=map(int,input().split())
 c=0
 m=10**9+7
 if w>=-9 and w<=8:
  for i in range(1,10):
   for j in range(10):
    if j-i==w:
     c+=1
  if n==2:
   print(c)
  elif n>2:
   c=((10**(n-2)%m)*(c%m))%m
   print(c)
 else:
  print(0)
