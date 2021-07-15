# cook your dish here
try:
 for _ in range(int(input())):
  n, m = map(int, input().split())
  l = []
  for j in range(n):
   l.append(list(input()))
  ans = []
  c = 0
  for u in range(m):
   for v in range(n):
    if l[v][u] == '1':
     c += 1
   ans.append(c)
   c = 0
  count = 0
  for j in range(len(ans)):
   count += ((ans[j] - 1) * (ans[j])) //2
  print(count)
except:
 pass
