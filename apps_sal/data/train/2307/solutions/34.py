(N, A, B) = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
ans = 0
for i in range(N - 1):
    ans += min((X[i + 1] - X[i]) * A, B)
print(ans)
