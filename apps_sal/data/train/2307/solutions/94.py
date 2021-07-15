n, a, b = map(int, input().split())
x = list(map(int, input().split()))

cnt = 0
for i, j in zip(x, x[1:]):
    if a * (j - i) < b:
        cnt += a * (j - i)
    else:
        cnt += b
print(cnt)
