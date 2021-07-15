for t in range(int(input())):
 n=int(input())
 a=sorted([int(i) for i in input().split()])
 s=0
 if n%2==0:
  i=0
  j=n-1
  while i<j:
   s+=abs(a[j]-a[i])
   j-=1
   i+=1
 else:
  s=a[n//2]
  while i<j:
   s+=abs(a[j]-a[i])
   j-=1
   i+=1
 print(s)
