# cook your dish here
EPS = 1e-8
EPS_ANS = 1e-3

for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    b = list(map(int, input().split()))
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    t_exit = l[0] / v[0]
    for i in range(1, n):
        if v[i] > 0:
            t_exit = min(t_exit, (l[i] - b[i]) / v[i])
        elif v[i] < 0:
            t_exit = min(t_exit, -b[i] / v[i])

    p = sum((b[i] - c[i]) ** 2 for i in range(n))
    q = sum(2 * (b[i] - c[i]) * v[i] for i in range(n))
    r = sum(vi ** 2 for vi in v)

    def func(t): return p / t / t + q / t + r

    def method1():
        if b == c:
            return 0
        lo, hi = 0, t_exit
        while hi - lo > EPS:
            d = (hi - lo) / 3
            m1 = lo + d
            m2 = m1 + d
            if func(m1) <= func(m2):
                hi = m2
            else:
                lo = m1
        return max(0, func(lo)) ** 0.5
    ans = method1()
    print('%.12f' % (ans,))
