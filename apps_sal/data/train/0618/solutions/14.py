for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    wsum = 0
    msum = 0
    for i in range(k):
        wsum += a[i]
    msum = max(wsum, msum)
    for i in range(k, n + k - 1):
        if i < n:
            wsum += a[i] - a[i - k]
        else:
            wsum += a[abs(n - i)] - a[i - k]
        msum = max(wsum, msum)
    print(msum)
