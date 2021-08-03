# cook your dish here
def gcd(m, n):
    if m > n:
        (a, b) = (n, m)
    else:
        (a, b) = (m, n)
    r = b
    while r > 1:
        r = b % a
        (a, b) = (r, a)
    if r == 0:
        return b
    else:
        return 1


def rlmaker(rl, pc, n):
    d = 1
    for i in range(0, pc + 1):
        if i < n - 1:
            rl[i] += pc // d
            d += 1
    return rl


def rlmakers(rl, pc, n):
    d = 1
    for i in range(0, pc + 1):
        if i < n - 1:
            if pc % d == 0:
                rl[i] += pc // d
            else:
                rl[i] += ((pc // d) + 1)
            d += 1
    return rl


def insFinder(n, l):
    lstone = 0
    rl = []
    for i in range(0, n - 1):
        rl.append(0)
    pathli = []
    pc = 0
    start = -1
    end = -1
    c = 0
    for i in range(0, n - 1):
        if gcd(l[i], l[i + 1]) != 1:
            if i == 0:
                start = 0
            if i == n - 2:
                end = n - 1
            if lstone == 1:
                pc += 1
            else:
                lstone = 1
                pc += 1
        else:
            if lstone == 1:
                pathli.append(pc)
                pc = 0
                lstone = 0

    if start == 0:
        if end == n - 1:
            if gcd(l[n - 1], l[0]) != 1:
                pathli.append(pc)
                if len(pathli) > 1:
                    pathli[0] += (pathli[len(pathli) - 1] + 1)
                    pathli.remove(pathli[len(pathli) - 1])
                else:
                    c = 1
                    pathli[0] += 1
            else:
                pathli.append(pc)
        else:
            if gcd(l[n - 1], l[0]) != 1:
                pathli[0] += 1
    else:
        if end == n - 1:
            if gcd(l[n - 1], l[0]) != 1:
                pc += 1
                pathli.append(pc)
            else:
                pathli.append(pc)
        else:
            if gcd(l[n - 1], l[0]) != 1:
                pathli.append(1)
    if c == 1:
        rl = rlmakers(rl, pathli[0], n)
    else:
        for i in range(0, len(pathli)):
            rl = rlmaker(rl, pathli[i], n)

    for i in range(0, n - 1):
        print(rl[i], end=' ')

    print("")


nt = int(input())
for i in range(0, nt):
    n = int(input())
    l = list(map(int, input().strip().split(' ')))
    insFinder(n, l)
