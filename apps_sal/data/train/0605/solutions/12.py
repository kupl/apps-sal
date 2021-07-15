t=int(input())
for _ in range(t):
 n,m=list(map(int,input().split()))
 s=input()
 flag=False
 for i in range(n):
  for j in range(m):
   x,y=i,j
   c=True
   for k in s:
    if k=='L':
     y-=1
    elif k=='U':
     x+=1
    elif k=='D':
     x-=1
    else:
     y+=1
    if x<0 or x>n-1 or y<0 or y>m-1:
     c=False
     break
   if c:
    flag=True
    break
  if flag:
   break
 if flag:
  print('safe')
 else:
  print('unsafe')

