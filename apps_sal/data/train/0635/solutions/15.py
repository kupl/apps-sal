
def compute_coeff(roots,k):
 mod = 10**9+7
 res = [1 for i in range(len(roots)+1) ]
 for i in range(len(roots)):
  cur_root = roots[i]
  for j in range(i,-1,-1):
   if j==0:res[j] *= -cur_root
   else:res[j] = res[j-1] - res[j]*cur_root
   if res[j] >=mod:res[j] %=mod
 for i in range(len(res)):res[i] = (abs(res[i])%mod)
 return res
n,k = map(int,input().split())
arr = list(map(int,input().split()))
d,a = dict(),0
for i in arr:
 if i not in d.keys():d[i] = 1
 else:d[i] += 1
ans = compute_coeff(list(d.values()),k)
ans = ans[::-1]
print(sum(ans[:k+1])%(10**9+7))
