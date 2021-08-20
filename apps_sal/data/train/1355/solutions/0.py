def index(n, val):
    while val >= n:
        val = val // 2
    return n - val


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    new = [0 for i in range(n)]
    for i in range(n):
        if arr[i] <= n:
            new[i] = arr[i] + arr[arr[i] - 1]
        else:
            new[i] = arr[index(n, arr[i]) - 1]
    print(*new)
