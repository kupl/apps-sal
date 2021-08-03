t = int(input())
while t > 0:
    n = int(input())
    arr = [int(x) for x in input().split()]
    low = arr[n - 1]
    bad = 0
    for i in range(n - 2, -1, -1):
        if arr[i] > low:
            bad += 1
        low = min(low, arr[i])
    print(bad)
    t -= 1
