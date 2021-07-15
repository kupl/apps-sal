t = int(input())
l1 = [[8,7],[8,4],[8,1],[7,5],[7,2],[5,4],[5,1],[4,2],[2,1]]
l2 = [[8,5],[8,2],[7,4],[7,1],[5,8],[5,2],[4,7],[4,1],[2,8],[2,5],[1,7],[1,4]]
length = 9
while t > 0 :
 t -= 1
 d = {}
 d2 = {}
 n = int(input())
 a = list(map(int,input().split()))
 bol = True
 for k in range(10) :
  d[k] = 0
  d2[k] = 0
 for i in range(n) :
  d[a[i]] += 1
  if bol and a[i] == 0 :
   bol = False
 if bol :
  print('-1')
 else :
  ans = ''
  for j in range(10) :
   if j % 3 != 0 :
    d2[j] = d[j]%3
    d[j] -= d2[j]
  for a,b in l1 :
   z = min(d2[a],d2[b])
   if z == 2 :
    d[a] += z
    d[b] += z
    d2[a] -= z
    d2[b] -= z

  for a,b in l2 :
   if d2[a] == 2 and d2[b] >= 1 :
    d[a] += 2
    d[b] += 1
    d2[a] -= 2
    d2[b] -= 1
  for a,b in l1 :
   z = min(d2[a],d2[b])
   if z > 0 :
    d[a] += z
    d[b] += z
    d2[a] -= z
    d2[b] -= z

  for _ in range(9,-1,-1) :
   ans += str(_)*d[_]
  print(ans)

