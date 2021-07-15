t=int(input())
for i in range(t):
 n=int(input())
 a=0
 for i in range(n):
  s,j=[int(x) for x in input().split()]
  if j-s>5:
   a+=1
 print(a)

