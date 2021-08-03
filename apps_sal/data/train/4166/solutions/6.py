from math import floor, sqrt


def solve(p):
    def powmod(x, n):
        res, cur = 1, x
        while n:
            if n & 1 == 1:
                res = (res * cur) % p
            cur = (cur * cur) % p
            n = n >> 1
        return res

    def invert(x):
        return powmod(x, p - 2)

    BLOCK = 1000
    base = 10

    baby = dict()
    bcur = base % p
    for i in range(1, BLOCK):
        if bcur not in baby:
            baby[bcur] = i
        else:
            break
        bcur = (bcur * base) % p

    step = invert(powmod(base, BLOCK))
    pcur = 1
    for j in range(0, p, BLOCK):
        ans = []

        def try_use(num, typ):
            if num in baby:
                totnum = j + baby[num]
                if totnum > 0:
                    ans.append((totnum, typ))
            if num == 1 and j > 0:
                ans.append((j, typ))

        try_use(pcur, 'sum')
        try_use(((p - 1) * pcur) % p, 'altsum')

        if ans:
            return '%d-%s' % min(ans)

        pcur = (pcur * step) % p
