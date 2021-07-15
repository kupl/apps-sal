for t in range(int(input())):
 n,m=map(int,input().split())
 l=list(map(int,input().split()))
 f=0
 for i in l:
  if i>=m:
   print("YES")
   f=1
   break
 if f==0:
  print("NO")
