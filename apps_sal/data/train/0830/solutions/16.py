for _ in range(int(input())):
 n = int(input())
 a = input()
 b = input()
 flag = 1
 for i in range(n):
  if a[i] < b[i]:
   flag = 0
   break
  if b[i] not in set(a):
   flag = 0
   break
 
 if flag == 1:
  d = {}
  for i in range(n):
   if a[i]!=b[i]:
    if b[i] not in d:
     d[b[i]]=[0]
    d[b[i]][0] += 1 
    d[b[i]] += [i]
  # print(d)
    
  cov = sorted(d,reverse=True)
  # print(cov)
  ans = []
  opr = len(cov)
  for i in cov:
   t = [d[i][0]+1]+[a.index(i)]+d[i][1:]
   # print(i)
   # print(t)
   ans.append(t)
  print(opr)
  for i in ans:
   print(*i, sep=' ')
 else:
  print(-1)
