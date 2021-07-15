n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
if all([a == b for a,b in ab]):
  print(0)
  return
ans = 0
diff = 10 ** 9
for a,b in ab:
  ans += b
  if a > b:
    diff = min(diff, b)
print(ans-diff)
