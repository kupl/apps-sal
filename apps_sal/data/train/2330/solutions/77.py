S = input()
n = len(S)
m = n // 2
if S[0] == '0' or S[-1] == '1':
  print(-1)
  return

ans = [[1, 2]]
node = 1
now = 3
for i in range(m):
  if S[i] != S[n-i-2]:
    print(-1)
    return
  else:
    if i == 0:
      continue
    ans.append([node, now])
    if S[i] == '0':
      now += 1
    else:
      node = now
      now += 1

for i in range(now, n+1):
  ans.append([node, i])

for a in ans:
  print(*a)
