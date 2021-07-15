n = int(input())
if n % 4 > 1: print(-1)
else:
    k = n // 2
    t = [0] * n
    for i in range(0, k, 2):
        t[i] = str(i + 2)
    for i in range(1, k, 2):
        t[i] = str(n - i + 1)
    if n & 1:
        k += 1
        t[k - 1] = str(k)
    for i in range(k, n, 2):
        t[i] = str(n - i - 1)
    for i in range(k + 1, n, 2):
        t[i] = str(i)
    print(' '.join(t))
