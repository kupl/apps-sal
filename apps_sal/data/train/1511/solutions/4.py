t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    s = list(input())
    ma, ir = [], []
    total = 0
    for i in range(n):
        k1 = s[i]
        if k1 == 'M':
            ma.append(i)
        elif k1 == 'I':
            ir.append(i)
        if k1 == 'X' or i == n - 1:
            alt = ir.copy()
            el = 0
            for mag in ma:
                for iron in ir:
                    if iron > mag:
                        sheet = 0
                        p = k + 1 - (iron - mag) - sheet
                        if p > 0:
                            el += 1
                            alt.remove(iron)
                            break
                    else:
                        sheet = 0
                        p = k + 1 - (mag - iron) - sheet
                        if p > 0:
                            el += 1
                            alt.remove(iron)
                            break
                ir = alt.copy()
            total += el
            s1 = set()
            ma, ir = [], []
    print(total)
