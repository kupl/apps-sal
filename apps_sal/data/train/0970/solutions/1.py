def binary(arr, s):
    low = 0
    high = n - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] <= s:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    arr.sort()
    for i in range(q):
        (x, y) = list(map(int, input().split()))
        s = x + y
        if arr[0] > s:
            print(0)
            continue
        if arr[0] == s:
            print(-1)
            continue
        index = binary(arr, s)
        if arr[index] == s:
            print(-1)
        else:
            print(index + 1)
