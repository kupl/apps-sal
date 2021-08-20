(n, a, b) = list(map(int, input().split()))
x = list(map(int, input().split()))
cnt = 0
for i in range(1, n):
    cnt += min(a * (x[i] - x[i - 1]), b)
print(cnt)
