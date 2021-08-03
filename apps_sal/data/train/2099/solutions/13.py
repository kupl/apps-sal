n, k = map(int, input().split())
t = list(range(1, n + 1))
if k > 1:
    j = 0
    for i in range((k + 1) // 2):
        t[j] = k - i + 1
        t[j + 1] = i + 1
        j += 2
    if not k & 1:
        t[j] = k // 2 + 1
print(' '.join(map(str, t)))
