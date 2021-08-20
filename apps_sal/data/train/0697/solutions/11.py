def func(a):
    S_max = 0
    for i in range(0, k):
        S_max += a[i]
    s = S_max
    for i in range(k, n):
        s += a[i] - a[i - k]
        S_max = max(S_max, s)
    return S_max


t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    print(func(a))
