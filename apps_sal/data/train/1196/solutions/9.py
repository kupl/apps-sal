t = int(input())
for tt in range(t):
    (n, m, k) = map(int, input().split())
    k -= 1
    arr = []
    for i in range(n):
        l = list(map(int, input().split()))
        arr.append(l)
    mm = 0
    for i in range(n):
        x = [0] * len(arr[i])
        x[0] = arr[i][0]
        for j in range(1, m):
            x[j] = x[j - 1] + arr[i][j]
        for j in range(m):
            if j + k < m:
                if j > 0:
                    mm = max(mm, x[j + k] - x[j - 1])
                else:
                    mm = max(mm, x[j + k])
    for i in range(m):
        x = []
        for j in range(n):
            x.append(arr[j][i])
        y = [0] * n
        y[0] = x[0]
        for j in range(1, n):
            y[j] = y[j - 1] + x[j]
        for j in range(n):
            if j + k < n:
                if j > 0:
                    mm = max(mm, y[j + k] - y[j - 1])
                else:
                    mm = max(mm, y[j + k])
    print(mm)
