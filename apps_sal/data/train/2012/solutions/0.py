n = int(input())
if n % 4 > 1:
    print(-1)
else:
    a = [n + 1 >> 1] * n
    for i in range(n // 4):
        j = i * 2
        (a[j], a[j + 1], a[-2 - j], a[-1 - j]) = (j + 2, n - j, j + 1, n - 1 - j)
    print(' '.join(map(str, a)))
