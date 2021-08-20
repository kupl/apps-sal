for __ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split())) + [0]
    L = [0] * (N + 2)
    R = [0] * (N + 2)
    for i in range(1, N + 1):
        L[i] = min(L[i - 1] + 1, arr[i])
    for i in range(N, 0, -1):
        R[i] = min(R[i + 1] + 1, arr[i])
    maxval = 0
    for i in range(1, N + 1):
        maxval = max(maxval, min(L[i], R[i]))
    print(sum(arr) - maxval ** 2)
