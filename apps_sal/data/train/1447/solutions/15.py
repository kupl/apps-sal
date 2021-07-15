def sol(n, l):
 no, oc, m, k = {}, {}, l[0], 1
 for i in range(1, n):
  if (l[i] != m):
   if m in no or k in oc: return "NO"
   else: no[m], oc[k] = True, True
   m, k = l[i], 1
  else: k += 1
 if m in no or k in oc: return "NO"
 return "YES"

for _ in range(int(input())):
 n = int(input())
 l = list(map(int, input().split()))
 print(sol(n, l))
