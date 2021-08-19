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
    n = II()
    aa = LI()
    bot = []
    mx = 0
    for (i, a) in enumerate(aa):
        if a > mx:
            bot.append((mx, i))
            mx = a
    aa.sort()
    ans = [0] * n
    j = n
    s = 0
    fin = 0
    for (mx, i) in bot[::-1]:
        while j > 0 and aa[j - 1] > mx:
            j -= 1
            s += aa[j]
        ans[i] = s - (n - j) * mx - fin
        fin += ans[i]
    print(*ans, sep='\n')


main()
