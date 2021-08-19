(N, A, B) = map(int, input().split())
X = list(map(int, input().split()))
sx = sorted(X)
ans = 0
for i in range(N - 1):
    d = sx[i + 1] - sx[i]
    if d * A < B:
        ans += d * A
    else:
        ans += B
print(ans)
