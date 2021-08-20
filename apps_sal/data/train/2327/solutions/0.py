import sys
input = sys.stdin.readline


def main():
    (n, m) = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(n)]
    BIT = [0] * (m + 2)

    def add(i, a):
        while i <= m + 1:
            BIT[i] += a
            i += i & -i

    def bit_sum(i):
        res = 0
        while i > 0:
            res += BIT[i]
            i -= i & -i
        return res
    for (l, r) in LR:
        add(l, 1)
        add(r + 1, -1)
    S = sorted([(r - l + 1, l, r) for (l, r) in LR])
    cnt = 0
    L = []
    for i in range(m, 0, -1):
        while S and S[-1][0] == i:
            (c, l, r) = S.pop()
            cnt += 1
            add(l, -1)
            add(r + 1, 1)
        res = cnt
        for j in range(0, m + 1, i):
            res += bit_sum(j)
        L.append(res)
    print(*L[::-1], sep='\n')


def __starting_point():
    main()


__starting_point()
