import sys
input = sys.stdin.readline

def main():
  n, m = map(int, input().split())
  S = [[] for _ in range(m+1)]
  for _ in range(n):
    l, r = map(int, input().split())
    S[r-l+1].append((l, r))
  
  BIT = [0]*(m+2)
  def add(i, a):
    while i <= m+1:
      BIT[i] += a
      i += i&(-i)
  def bit_sum(i):
    res = 0
    while i > 0:
      res += BIT[i]
      i -= i&(-i)
    return res
  cnt = n
  for i in range(1, m+1):
    for l, r in S[i]:
      cnt -= 1
      add(l, 1)
      add(r+1, -1)
    res = cnt
    for j in range(0, m+1, i):
      res += bit_sum(j)
    print(res)

def __starting_point():
  main()
__starting_point()
