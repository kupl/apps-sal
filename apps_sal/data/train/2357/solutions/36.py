import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
mod = 10 ** 9 + 7
dsm = M - sum(a)
if dsm < 0:
  print(0)
  return

class Factorial:
  def __init__(self, n, mod):
    self.mod = mod
    self.f = [1]
    for i in range(1, n + 1):
      self.f.append(self.f[-1] * i % mod)
    self.i = [pow(self.f[-1], mod - 2, mod)]
    for i in range(1, n + 1)[: : -1]:
      self.i.append(self.i[-1] * i % mod)
    self.i.reverse()
  def factorial(self, i): return self.f[i]
  def ifactorial(self, i): return self.i[i]
  def combi(self, n, k): return self.f[n] * self.i[n - k] % self.mod * self.i[k] % self.mod
  def permi(self, n, k): return self.f[n] * self.i[n - k] % self.mod

sm = sum(a)
res = Factorial(sm + N, mod).ifactorial(sm + N)
for x in range(N + M, N + M - sm - N, -1):
  res *= x
  res %= mod
print(res)
