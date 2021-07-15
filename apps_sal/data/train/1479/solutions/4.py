n=int(input())
while n>0:
 t=int(input())
 a=[]
 for i in range(8):
  a.append(0)
 for i in range(t):
  b,c=[int(x) for x in input().split()]
  if b<=8 and c>a[b-1]:
   a[b-1]=c
 print(sum(a))
 n=n-1

