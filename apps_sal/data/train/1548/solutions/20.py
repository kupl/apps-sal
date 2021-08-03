for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        arr[i] = min(arr[i], arr[i - 1] + 1)
    for i in range(n - 2, -1, -1):
        arr[i] = min(arr[i], arr[i + 1] + 1)
    print(*arr)
