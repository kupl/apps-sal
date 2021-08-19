def solve():
    n1, m, a, d = list(map(int, input().split()))
    t = list(map(int, input().split()))
    from bisect import insort
    from math import floor
    insort(t, a * n1)
    pred = 0
    k = 0
    kpred = 0
    n = 0
    step = d // a + 1
    sol = 0
    fl = 0
    for i in t:
        if (i > pred):
            if fl == 0:
                n = (i - pred + (pred % a)) // a
                if n != 0:
                    k += (n // step) * step - step * (n % step == 0) + 1
                    if k > n1:
                        k = n1
                        fl = 1
                # print(k)
                if (k * a + d >= i) and (n != 0):
                    pred = k * a + d
                else:
                    pred = i + d
                    k = floor(pred // a)
                    sol += 1
                # if n==0:
                k = min(floor(pred // a), n1)
                sol += n // step + (n % step != 0)
            else:
                sol += 1
                pred = i + d
        if i == a * n1:
            fl = 1
            # print(i,pred,sol,n,step,k, fl)
    print(sol)


solve()
