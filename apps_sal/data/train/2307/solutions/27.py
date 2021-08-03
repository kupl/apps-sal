def LI():
    return list(map(int, input().split()))


N, A, B = LI()
X = LI()
ans = 0
for i in range(N - 1):
    ans += min((X[i + 1] - X[i]) * A, B)
print(ans)
