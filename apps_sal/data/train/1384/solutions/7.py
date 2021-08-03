for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = str(input())
    m = 0
    for i in range(n - k + 1):
        count, j, l = k, i - 1, i + k
        while j > -1 and j < n:
            if arr[j] == '1':
                count, j = count + 1, j - 1
            else:
                break
        while l < n and l > -1:
            if arr[l] == '1':
                count, l = count + 1, l + 1
            else:
                break
        m = max(m, count)
    print(m)
