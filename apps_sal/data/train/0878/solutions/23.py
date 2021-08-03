t = int(input())
for i in range(t):
    n, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    arr.insert(0, 0)
    count = 0
    p = 0
    q = 0
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] <= k:
            pass
        elif arr[i + 1] - arr[i] > k:
            p = arr[i + 1]
            q = arr[i]
            while p - q > k:
                q = q + k
                count += 1
    print(count)
