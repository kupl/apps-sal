t = int(input())
for _ in range(t):
    (n, m, k) = list(map(int, input().split()))
    main = []
    for i in range(n):
        l = list(map(int, input().split()))
        main.append(l)
    maxi = 0
    for i in range(n):
        q = main[i]
        sum1 = sum(q[0:k])
        i = 0
        j = k - 1
        while j < m:
            if maxi < sum1:
                maxi = sum1
            j += 1
            if j < m:
                sum1 += q[j]
            i += 1
            sum1 -= q[i - 1]
    new = []
    for i in range(m):
        l = [0] * n
        new.append(l)
    for i in range(n):
        for j in range(m):
            new[j][i] = main[i][j]
    for i in range(m):
        q = new[i]
        sum1 = sum(q[0:k])
        i = 0
        j = k - 1
        while j < n:
            if maxi < sum1:
                maxi = sum1
            j += 1
            if j < n:
                sum1 += q[j]
            i += 1
            sum1 -= q[i - 1]
    print(maxi)
