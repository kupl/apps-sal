N = int(input())
A = list(map(int, input().split()))
all = 0
for a in A:
  all = all ^ a
ans = []
for a in A:
  ans.append(all ^ a)
print(*ans)
