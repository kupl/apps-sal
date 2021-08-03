for f in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    nh = n // 2
    su = [0] * (2 * k + 1)
    mi = [0] * nh
    ma = [0] * nh
    for i in range(nh):
        su[a[i] + a[-i - 1]] += 1
        mi[i] = min(a[i], a[-i - 1]) + 1
        ma[i] = max(a[i], a[-i - 1]) + k
    mi.sort()
    ma.sort()
    mii = 0
    maa = 0
    sol = n
    for i in range(2 * k + 1):
        while mii < nh and mi[mii] <= i:
            mii += 1
        while maa < nh and ma[maa] < i:
            maa += 1
        sol = min(sol, n - su[i] - mii + maa)
    print(sol)
