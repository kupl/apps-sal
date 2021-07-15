t=int(input())

for _ in range(t):
 n,q=map(int,input().split())
 s=input()
 l=[0]*(n-1)
 for i in range(n-2):
  a,b,c=s[i],s[i+1],s[i+2]
  if len(set([a,b,c]))<3:
   l[i]=l[i-1]+1
  else:
   l[i]=l[i-1]
   
 for i in range(q):
  left,right=map(int,input().split())
  left-=1
  right-=1
  if right-left+1 <3:
   print('NO')
   continue
  if (l[right-2]-l[left-1])>0:
   print('YES')
  else:
   print('NO')
