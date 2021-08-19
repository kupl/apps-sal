(n, a, b) = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = [X[i + 1] - X[i] for i in range(n - 1)]
ans = 0
for y in Y:
    if y * a <= b:
        ans += y * a
    else:
        ans += b
print(ans)
