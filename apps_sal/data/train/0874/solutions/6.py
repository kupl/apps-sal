for _ in range(int(input())):
    (N, m, s) = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    count = 0
    arr.sort()
    while i < len(arr) and m > 1:
        if arr[i] <= s:
            m -= 1
            count += 1
        elif arr[i] % s == 0:
            if arr[i] // s <= 2:
                m = m - arr[i] // s
                count += 1
        elif arr[i] // s + 1 <= 2:
            m = m - (arr[i] // s + 1)
            count += 1
        i += 1
    while m > 0 and i < len(arr):
        if arr[i] <= s:
            count += 1
            m = m - 1
        elif arr[i] % s == 0:
            if arr[i] // s <= m:
                m = m - arr[i] // s
                count += 1
        elif arr[i] // s + 1 <= m:
            m = m - (arr[i] // s + 1)
            count += 1
        i += 1
    print(count)
