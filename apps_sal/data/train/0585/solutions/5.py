try:

    def gcd_fd(i, j):
        while j:
            (i, j) = (j, i % j)
        return i

    def gcd_l(t):
        num = t[0]
        k = t[1]
        gcd = gcd_fd(num, k)
        for i in range(2, len(t)):
            gcd = gcd_fd(gcd, t[i])
        return gcd

    def fact(num1):
        if num1 == 0:
            return 1
        a = []
        for j in range(1, int(num1 ** (1 / 2)) + 1):
            if num1 % j == 0:
                a.append(j)
                a.append(num1 // j)
        return a
    for _ in range(int(input())):
        (n, m) = map(int, input().split())
        a = list(map(int, input().split()))
        p = 0
        ans = 0
        if m > 1:
            p = gcd_l(a)
        else:
            p = a[0]
        fac = fact(p)
        fac.sort(reverse=True)
        for i in fac:
            if i <= n:
                ans = n - i
                break
        print(ans)
except:
    pass
