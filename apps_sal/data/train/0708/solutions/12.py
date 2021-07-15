def solve():
 N, K = map(int, input().split())
 mod = 10**9 + 7
 m = 0
 for i in range(1, N+1):
  c = pow(K, 2 * i - 1, mod)
  K *= c
  K %= mod
  m += c
  m %= mod
 print(m)


def __starting_point():
 t = int(input())
 while t != 0:
  solve()
  t -= 1
__starting_point()
