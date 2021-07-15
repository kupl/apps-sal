N = int(input())
diff_a_b = []
for i in range(N):
  a, b = map(int, input().split())
  diff_a_b.append([a - b, a, b])

diff_a_b.sort()
if diff_a_b[0][0] == 0: # 最初から数列が等しい
  print(0)
  return

ans = 0
d = 0
temp = 10**10
for diff, a, b in diff_a_b:
  if diff <= 0: # a <= b
    ans += b
    d -= diff
  else:
    ans += b
    temp = min(temp, b)

print(ans - temp)
