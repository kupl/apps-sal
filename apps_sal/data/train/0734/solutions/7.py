R = lambda: map(int, input().split())
for _ in range(int(input())):
 n = int(input())
 L1 = list(R())
 L = sorted(L1)
 d = {}
 f = 0
 p = n//2
 for i in range(n):
  if L[i] not in d:d[L[i]] = [0, []]
  d[L[i]][0] += 1
  d[L[i]][1] += [i]
  if d[L[i]][0] > p:f = 1;break
 if f:print("No")
 else:
  print("Yes")
  res = []
  #print(d)
  for i in L1:
   ind = d[i][1].pop()
   if n%2 and ind == n-1:
    res.append(L[0])
    continue
   if ind+p < n:
    res.append(L[ind+p])
   elif ind-p >= 0:
    res.append(L[ind-p])
  print(*res)
