test = int(input())
for _ in range(test):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    days = 0
    for i in range(n):
        if arr[i] > x:
            while x < arr[i]:
                x = x * 2
                days = days + 1
            days = days + 1
            x = 2 * arr[i]
        else:
            days = days + 1
            x = max(x, 2 * arr[i])
    print(days)
