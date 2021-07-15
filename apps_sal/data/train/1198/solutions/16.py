import math
import bisect

def inn():
 return int(input())

def inl():
 return list(map(int, input().split()))

MOD = 10**9+7
INF = inf = 10**18+5

n = inn()
a = inl()

ans = {}
is_gcd = [0]*1000001
ans[1] = 0
for i in range(n):
 cur_gcd = a[i]
 for j in range(i, n):
  cur_gcd = math.gcd(cur_gcd, a[j])
  if cur_gcd==1:
   ans[1] += (n-j)
   break
  elif cur_gcd<1000001:
   if is_gcd[cur_gcd]==0:
    is_gcd[cur_gcd] = 1
    ans[cur_gcd] = 0
   ans[cur_gcd] += 1
# print(ans)

keys = list(ans.keys())
ans1 = [0]*1000001
for i in keys:
 for j in range(i, 1000001, i):
  ans1[j] += ans[i]
# print(ans1[:10])

for q in range(inn()):
 k = inn()
 print(ans1[k])
