N, A, B = map(int, input().split())

X = list(map(int, input().split()))
ans = 0
for i in range(1, N):
  dist = X[i] - X[i-1]
  ans += min(A*dist , B)

print(ans)
