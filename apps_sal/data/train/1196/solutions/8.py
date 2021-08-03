t = int(input().strip())
for p in range(t):
    n, m, k = input().strip().split()
    n, m, k = int(n), int(m), int(k)
    arr = []
    rmax = []
    cmax = []
    for i in range(n):
        arr2 = list(map(int, input().strip().split()))
        arr.append(arr2)
        row_sum = []
        row_sum.append(sum(arr2[:k]))
        for j in range(1, m - k + 1):
            row_sum.append(row_sum[j - 1] - arr2[j - 1] + arr2[j + k - 1])
        rmax.append(max(row_sum))
    for i in range(m):
        col_sum = []
        s = 0
        for j in range(k):
            s += arr[j][i]
        col_sum.append(s)
        for j in range(1, n - k + 1):
            col_sum.append(col_sum[j - 1] - arr[j - 1][i] + arr[j + k - 1][i])
        cmax.append(max(col_sum))
    print(max(max(rmax), max(cmax)))
