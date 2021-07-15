read = lambda: list(map(int, input().split()))
read_s = lambda: list(map(str, input().split()))

n, m = read()
ans = 0
while True:
 if n > m:
  ans += m
  n -= 2*m
 else: break
print(ans)
