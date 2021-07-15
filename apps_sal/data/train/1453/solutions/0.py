n, q, k = map(int, input().split())
arr = list(map(int, input().split()))
query = list(input())
q_ = len(query)
c1 = query.count('?')
c = arr.count(0)
if c == n:
 for i in range(c1):
  print(0)
else:
 for i in range(q_):
  if (i!=0) and (query[i] == '?' and query[i-1] == '?'):
   print(max_c)
  elif query[i] == '?':
   max_c = cnt = 0
   for j in range(n):
    if (j != n - 1) and (arr[j] == 1 and arr[j + 1] == 1):
     cnt += 1
    else:
     max_c = max(max_c, cnt + 1)
     cnt = 0
    if k < max_c:
     max_c = k
     break
   print(max_c)
  elif query[i] == '!':
   temp = arr[n - 1]
   del arr[n - 1]
   arr.insert(0, temp)
