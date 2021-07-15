mod = 10**9 + 7

def solve(n, m):
 ans = n*(n-1) % mod
 if m==1:
  print(ans)
  return
 else:
  ans = (ans * pow(n-1, m-1, mod)) % mod

 print(ans)
 
for case in range(int(input())):
 n,m = list(map(int, input().split()))

 solve(n, m)

