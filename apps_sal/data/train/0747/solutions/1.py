t=int(input())
while t>0:
 t-=1
 n=int(input())
 a=list(map(int,input().split()))
 b=set()
 c=[]
 for i in a:
  if i not in b:
   b.add(i)
  else:
   c.append(i)
 b=list(b)
 b.sort()
 c.sort(reverse=True)
 e=b+c
 k=0
 for i in range(len(e)-1):
  if e[i]==e[i+1]:
   k=1
   print("NO")
   break
 if k==0:
  print("YES")
  print(*e)
