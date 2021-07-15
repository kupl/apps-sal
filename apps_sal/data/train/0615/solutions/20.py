n=int(input())
while(n>0):
 l=list(map(int,input().split()))
 l1=list(map(int,input().split()))
 while(l[1]>0):
  l2=list(map(int,input().split()))
  s=0
  for i in range(l2[0]-1,l2[1]):
   s=s+l1[i]
  print(s)
  l[1]=l[1]-1
 n=n-1

