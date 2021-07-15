t = int(input())
for _ in range(t):
 n = int(input())
 arr = list(map(int,input().split()))
 q = int(input())
 s = [0 for i in range(n)]
 ev = 0
 for i in range(n):
  if arr[i]%2==0:
   ev+=1
  s[i] = ev
 for i in range(q):
  l,r = list(map(int,input().split()))
  l-=1
  r-=1
  if arr[l]%2==0 or arr[r]%2==0:
   print('EVEN')
   continue
  diff = s[r] - s[l]
  if diff>0:
   print('EVEN')
  else:
   print('ODD')

