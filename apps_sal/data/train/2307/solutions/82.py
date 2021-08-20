(N, A, B) = list(map(int, input().split()))
X = list(map(int, input().split()))
NewX = []
for i in range(N - 1):
    NewX.append((X[i + 1] - X[i]) * A)
ans = 0
for i in NewX:
    ans += min(i, B)
print(ans)
