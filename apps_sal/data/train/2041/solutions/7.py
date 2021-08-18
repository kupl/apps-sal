3


def needs_rep(t, i):
    if i % 2 == 0:
        return t[i] >= t[i + 1]
    else:
        return t[i] <= t[i + 1]


def would_need_rep(t, i, j1, j2):
    n = len(t)
    if i < 0:
        return False
    if i >= n - 1:
        return False

    tj1 = t[j2]
    tj2 = t[j1]

    ti = t[i]
    if i == j1:
        ti = tj1
    if i == j2:
        ti = tj2

    ti1 = t[i + 1]
    if i + 1 == j1:
        ti1 = tj1
    if i + 1 == j2:
        ti1 = tj2

    if i % 2 == 0:
        return ti >= ti1
    else:
        return ti <= ti1


def main():
    n = int(input())
    t = [int(i) for i in input().split()]

    rep = []
    for i in range(n - 1):
        if needs_rep(t, i):
            rep.append(i)

    if(len(rep) > 4):
        print(0)
        return

    to_try = [rep[0], rep[0] + 1]

    s = set()

    for i in to_try:
        for j in range(n):
            if i == j:
                continue

            if would_need_rep(t, i, i, j):
                continue
            if would_need_rep(t, i - 1, i, j):
                continue
            if would_need_rep(t, j, i, j):
                continue
            if would_need_rep(t, j - 1, i, j):
                continue

            bad = False
            for r in rep:
                if would_need_rep(t, r, i, j):
                    bad = True
            if bad:
                continue

            if (i, j) not in s and (j, i) not in s:
                s.add((i, j))

    print(len(s))


def __starting_point():
    main()


__starting_point()
