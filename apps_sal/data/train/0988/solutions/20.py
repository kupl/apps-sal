

def solve():
 twopow = {}
 for i in range(31):twopow[i] = 2**i
 for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = dict()
  for i in range(31):b[i] = 0
  original_tot = 0
  for i in range(n):
   s = bin(a[i])[2:]
   s = s[::-1]
   original_tot += a[i]
   for i in range(len(s)):
    if s[i] == '1':
     b[i] += 1
  change = 0
  for x in b:
   p = b[x]
   if p > 0:
    if p > n - p:
     change += (p - (n - p)) * (twopow[x])

  original_tot -= change
  print(original_tot)

solve()


