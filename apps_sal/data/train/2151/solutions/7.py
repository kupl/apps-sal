def __starting_point():
    n, s = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    arr.sort()
    mid = n // 2
    ans = 0
    if s == arr[mid]:
        print(ans)
    elif s > arr[mid]:
        while mid < n and arr[mid] < s:
            ans += s - arr[mid]
            mid += 1
        print(ans)
    else:
        while mid >= 0 and arr[mid] > s:
            ans += arr[mid] - s
            mid -= 1
        print(ans)
__starting_point()
