(n, h) = list(map(int, input().split()))
ans = []
for i in range(1, n):
    ans.append((i / n) ** 0.5 * h)
print(' '.join(map(str, ans)))
