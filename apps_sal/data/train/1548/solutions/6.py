t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_modified = [-1 for _ in range(n)]
    for i in range(n):
        arr_modified[i] = arr[i] + i
    minRights = [arr_modified[-1] for _ in range(n)]
    for i in range(n - 2, -1, -1):
        minRights[i] = min(arr_modified[i], minRights[i + 1])
    minLeft = float('inf')
    soldValues = [-1 for _ in range(n)]
    for i in range(n):
        soldValues[i] = min(minLeft, minRights[i] - i)
        minLeft = min(minLeft + 1, arr[i] + 1)
    print(' '.join((str(x) for x in soldValues)))
