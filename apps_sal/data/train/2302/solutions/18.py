import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def main():
    (dn, s) = MI()
    dd = LI()
    qn = II()
    qq = LI()
    qi = [(q - 1, i) for (i, q) in enumerate(qq)]
    pos = [s]
    for d in dd:
        pos.append(min(pos[-1], abs(d - pos[-1])))
    bb = [1] * (dn + 1)
    for i in range(dn - 1, -1, -1):
        d = dd[i]
        if d < bb[i + 1] * 2:
            bb[i] = bb[i + 1] + d
        else:
            bb[i] = bb[i + 1]
    ans = [''] * qn
    for (q, ai) in qi:
        if pos[q] >= bb[q + 1]:
            ans[ai] = 'YES'
        else:
            ans[ai] = 'NO'
    print(*ans, sep='\n')


main()
