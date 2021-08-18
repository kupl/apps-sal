from math import ceil

for _ in range(int(input())):
    n, h = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    low, high = 1, max(arr)
    while(low != high):
        check = 0
        mid = (low + high) // 2
        for i in range(n):
            check += (ceil(arr[i] / mid))
        if check <= h:
            high = mid
        else:
            low = mid + 1
    print(low)
