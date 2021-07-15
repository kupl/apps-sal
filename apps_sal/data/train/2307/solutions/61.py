N, A, B = map(int, input().split())
X = list(map(int, input().split()))
ans = (X[-1] - X[0]) * A
for x1, x2 in zip(X, X[1:]):
    if (x2 - x1) * A > B:
        ans -= (x2 - x1) * A - B
print(ans)
