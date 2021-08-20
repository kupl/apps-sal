for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    m = max(a)
    if k >= m:
        print(n)
        continue
    else:
        c = 0
        while k < m:
            f = 0
            for i in range(n):
                if a[i] <= k and a[i] > k // 2:
                    f = 1
                    k = 2 * a[i]
                    a[i] = 0
                    break
            if f == 0:
                k = k * 2
            c += 1
        for i in range(n):
            if a[i] != 0:
                c += 1
        print(c)
