t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = max(arr)
    for i in range(n - 1, -1, -1):
        if arr[i] == maxi:
            r = i
            break
    for i in range(n):
        if arr[i] == maxi:
            r = r - i
            break
    if n // 2 - r < 0:
        print(0)
    else:
        print(n // 2 - r)
