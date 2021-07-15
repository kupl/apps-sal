for _ in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 p = []; cnt = 0
 for i in range(n):
  if a[i]%2==0:
   cnt += 1
   p.append(cnt)
   cnt += 1
   continue
  p.append(cnt)
 for _ in range(int(input())):
  l,r = list(map(int,input().split()))
  if p[r-1]-p[l-1]>0:
   print('EVEN')
  else:
   print('ODD')

