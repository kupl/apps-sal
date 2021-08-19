for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = a + a[:k]
    s = sum(a[:k])
    maxsum = s
    for i in range(k, len(a)):
        s = s + a[i] - a[i - k]
        maxsum = max(maxsum, s)
    print(maxsum)
