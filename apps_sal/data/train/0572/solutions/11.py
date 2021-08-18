t = int(input())
for i in range(0, t):
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    k = arr[2]
    if m > n:
        n, m = m, n
    diff = n - m
    if diff == k:
        print(0)
    elif diff > k:
        print(diff - k)
    else:
        print(0)
