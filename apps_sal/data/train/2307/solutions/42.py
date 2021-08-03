n, a, b = map(int, input().split())
x_seq = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    dis = x_seq[i + 1] - x_seq[i]
    ans += min(dis * a, b)
print(ans)
