for T in range(int(input())):
    n = int(input())
    arr = [0] + [int(x) for x in input().split()] + [0]
    L = [0] * (n + 2)
    R = [0] * (n + 2)
    k = 0
    for i in range(1, n + 1):
        L[i] = min(L[i - 1] + 1, arr[i])
    for i in range(n, 0, -1):
        R[i] = min(R[i + 1] + 1, arr[i])
    maxHeight = 0
    for i in range(1, n + 1):
        height = min(L[i], R[i])
        maxHeight = max(maxHeight, height)
    print(sum(arr) - maxHeight**2)
