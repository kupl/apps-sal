import time
vowels = 'aeiou'
start_time = time.time()


def main():
    import math as m
    ryt = m.log(10**7, 2)
    lyt = m.log(0.0000009, 2)
    t = int(input())
    v = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
    for qwer in range(t):
        l = int(input())
        a = []
        b = []
        for wer in range(l):
            s = input()
            n = len(s)
            c1 = 0
            for i in range(n):
                if s[i] not in v:
                    if i + 1 < n:
                        if s[i + 1] not in v:
                            c1 = 1
                            break
                    if i + 2 < n:
                        if s[i + 2] not in v:
                            c1 = 1
                            break
            if c1 == 1:
                b.append(s)
            else:
                a.append(s)
        xa = {}
        fxa = {}
        xb = {}
        fxb = {}
        ka = len(a)
        kb = len(b)
        for i in range(ka):
            d = {}
            for j in range(len(a[i])):
                if a[i][j] in d:
                    d[a[i][j]] += 1
                else:
                    d[a[i][j]] = 1
            for u in d:
                if u in xa:
                    xa[u] += 1
                    fxa[u] += d[u]
                else:
                    xa[u] = 1
                    fxa[u] = d[u]
        for i1 in range(kb):
            d = {}
            for j1 in range(len(b[i1])):
                if b[i1][j1] in d:
                    d[b[i1][j1]] += 1
                else:
                    d[b[i1][j1]] = 1
            for u1 in d:
                if u1 in xb:
                    xb[u1] += 1
                    fxb[u1] += d[u1]
                else:
                    xb[u1] = 1
                    fxb[u1] = d[u1]
        ans = 0
        for y in xa:
            ans += m.log(xa[y], 2) - ka * (m.log(fxa[y], 2))
        for r in xb:
            ans += kb * (m.log(fxb[r], 2)) - m.log(xb[r], 2)
        if ans > ryt:
            print("Infinity")
        elif ans < lyt:
            print(0)
        else:
            print(2**ans)


main()
