for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr + [0]
    L = [0] * (n + 2)
    for i in range(1, n + 1):
        L[i] = min(L[i - 1] + 1, arr[i])
    R = [0] * (n + 2)
    for i in range(n, 0, -1):
        R[i] = min(R[i + 1] + 1, arr[i])
    ma = 0
    for i in range(1, n + 1):
        l = min(L[i], R[i])
        ma = max(ma, l)

    ans = sum(arr) - ma**2
    print(ans)
