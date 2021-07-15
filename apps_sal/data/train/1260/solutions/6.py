# cook your dish here
for _ in range(int(input())):
 n,m,k = list(map(int, input().split()))
 
 l = [[] for _ in range(n+1)]
 for _ in range(m):
  a,b = list(map(int, input().split()))
  l[a].append(b)
  l[b].append(a)
 m_l = [-1] + list(map(int, input().split()))
 
 visited = [False for _ in range(n+1)]
 
 sum_l = []
 for i in range(1, n+1):
  if visited[i] == False:
   summa = 0
   q = [i]
   while len(q) != 0:
    v = q[-1]
    del q[-1]
    if visited[v]:
     continue
    
    visited[v] = True
    summa += m_l[v]
    for vv in l[v]:
     q.append(vv)
   sum_l.append(summa)
   
 # print(sum_l)
 if len(sum_l) < k:
  print(-1)
 else:
  sum_l.sort()
  if k % 2 == 0:
   k //= 2
   ans = sum(sum_l[:k]+sum_l[-k:])
  else:
   k //= 2
   ans = sum_l[-k-1]
   if k > 0:
    ans += sum(sum_l[:k]+sum_l[-k:])
  print(ans)
   

