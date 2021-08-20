import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def main():
    inf = 10 ** 7
    s = input()
    n = len(s)
    s += ''.join((chr(i + 97) for i in range(26)))
    size = [0] * 26
    pos = [n + i for i in range(26)]
    nxt = [-1] * n
    for i in range(n - 1, -1, -1):
        min_size = inf
        min_pos = -1
        for (sz, p) in zip(size, pos):
            if sz < min_size:
                min_size = sz
                min_pos = p
        code = ord(s[i]) - 97
        size[code] = min_size + 1
        pos[code] = i
        nxt[i] = min_pos
    min_size = inf
    min_pos = -1
    for (sz, p) in zip(size, pos):
        if sz < min_size:
            min_size = sz
            min_pos = p
    i = min_pos
    ans = s[i]
    while i < n:
        i = nxt[i]
        ans += s[i]
    print(ans)


main()
