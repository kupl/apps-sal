from sys import stdin
def gt(num):
 if num:
  return num
 return 0
for __ in range(int(stdin.readline().split()[0])):
 n = int(stdin.readline().split()[0])
 a = list(map(int, stdin.readline().split()))
 cnta = dict()
 cnta.setdefault(0)
 cntb = dict()
 cntb.setdefault(0)
 for i in a:
  cnta[i] = gt(cnta.get(i)) + 1
 asum = 0
 bsum = sum(a)
 ans = 0
 for i in range(n-1):
  asum += a[i]
  bsum -= a[i]
  cnta[a[i]] = gt(cnta.get(a[i])) - 1
  cntb[a[i]] = gt(cntb.get(a[i])) + 1
  ans += gt(cnta.get(bsum-asum))
  ans += gt(cntb.get(asum-bsum))
 print(ans)
