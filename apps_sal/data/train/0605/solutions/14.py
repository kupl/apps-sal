

t = int(input())


for _ in range(t):
 n,m = list(map(int,input().split()))
 s = input()
 flag = 0
 for i in range(n):
  for j in range(m):
   x = i
   y = j
   for k in s:
    if k == 'L':
     y-=1
    elif k == 'U':
     x-=1
    elif k == 'D':
     x+=1
    elif k == 'R':
     y+=1

    if x<0 or x>=n or y<0 or y>=m:
     break

   if 0<=x<=n-1 and 0<=y<=m-1:
    flag = 1
    break
  if flag == 1:
   break
 if flag == 1:
  print('safe')
 else:
  print('unsafe')







