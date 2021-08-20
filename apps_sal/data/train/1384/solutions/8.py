for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = str(input())
    m = 0
    for i in range(n - k + 1):
        count = k
        j = i - 1
        while j > -1 and j < n:
            if arr[j] == '1':
                count += 1
                j -= 1
            else:
                break
        l = i + k
        while l < n and l > -1:
            if arr[l] == '1':
                count += 1
                l += 1
            else:
                break
        if count > m:
            m = count
    print(m)
