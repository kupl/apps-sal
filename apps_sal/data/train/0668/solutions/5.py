def maxsubarraysum(arr):
    max_till = arr[0]
    max_cur = arr[0]
    n = len(arr)
    for i in range(1, n):
        max_cur = max(arr[i], max_cur + arr[i])
        max_till = max(max_cur, max_till)
    return max_till


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    arr = [int(i) for i in input().split()]
    if m == 1:
        print(maxsubarraysum(arr))
    else:
        arr2 = arr + arr
        if m == 2:
            print(maxsubarraysum(arr2))
        else:
            maxsum2 = maxsubarraysum(arr2)
            if sum(arr) >= 0:
                print(maxsum2 + (m - 2) * sum(arr))
            else:
                print(maxsum2)
