t = int(input())
for _ in range(t):
 n, k = map(int,input().split())
 li = list(input().split())
 h = li.count('H')
 t = n - h
 #print(h, t)
 for i in range(k):
  d= li[-1]
  #print(li)
  li = li[:-1]
  #print(li, d)
  if d == 'T':
   t = t - 1
  else:
   h, t = t, h - 1
   li = ['H' if li[j] == 'T' else 'T' for j in range(n - i - 1) ]
  #print(li)
 print(h)
