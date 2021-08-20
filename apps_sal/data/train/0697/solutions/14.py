for _ in range(int(input())):
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr[:k])
    m = s
    for i in range(1, n - k + 1):
        s = s - arr[i - 1] + arr[i + k - 1]
        if s > m:
            m = s
    print(m)
