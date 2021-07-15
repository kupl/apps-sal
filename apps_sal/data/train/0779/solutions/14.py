t=int(input())
while t>0:
 n=int(input())
 li=input().split()
 for i in range(n):
  li[i]=int(li[i])
 n-=1
 li.sort()
 while n>0:
  li[n-1]=(li[n]+li[n-1])/2
  n-=1
 print(li[0])
 t-=1
