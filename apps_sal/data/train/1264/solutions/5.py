read = lambda: list(map(int, input().split()))
read_s = lambda: list(map(str, input().split()))

n, m = read()
ans = 0
while n > 0:
 if n > m:
  ans += m
  n -= 2*m
 else:
  ans += 1
  n -= 2
print(ans)
