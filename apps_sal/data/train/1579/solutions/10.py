for t in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 s=set()
 f=1
 for i in range(n):
  a=l[i]
  for j in range(i,n):
   a|=l[j]
   if(a in s):
    print('NO')
    f=0
    break
   s.add(a)
  if(f==0):
   break
 if(f):
  print('YES')
