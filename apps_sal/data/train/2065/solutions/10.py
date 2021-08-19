(n, k) = map(int, input().split())
for _ in range(k):
    a = list(map(int, input().split()))[1:] + [0]
    if a[0] != 1:
        continue
    i = 0
    while a[i + 1] == i + 2:
        i += 1
print(2 * n - k - 1 - 2 * i)
