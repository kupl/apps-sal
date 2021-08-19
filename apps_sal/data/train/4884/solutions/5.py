from string import ascii_lowercase as lu


def connect_the_dots(li):
    li = [[j for j in i] for i in li.splitlines()]

    def find_char(c): return next(([i, k] for i, j in enumerate(li) for k, l in enumerate(j) if l == c), 0)  # find next char from string/array

    lower = iter(lu)

    char, chars = find_char(next(lower)), []

    while char:
        chars.append(char)
        char = find_char(next(lower))

    def A(s, se, see, e, ee, eee): return list(zip(list(range(s, se + 1, see)), list(range(e, ee + 1, eee))))  # for diagonals

    for h, g in zip(chars, chars[1:]):
        i, j = h
        k, l = g
        m, m1, n, n1 = min(i, k), min(j, l), max(i, k), max(j, l)
        if i == k:                      # horizontal
            while m1 <= n1:
                li[i][m1] = '*'
                m1 += 1
        elif j == l:                    # verical
            while m <= n:
                li[m][j] = '*'
                m += 1
        else:                           # diagonals
            B, C = i > k, j > l
            for o, p in A(i, k - (2 if B else 0), (1 if not B else -1), j, l - (2 if C else 0), (1 if not C else -1)):
                li[o][p] = '*'
        i, j = k, l
    return "\n".join(["".join(i) for i in li]) + "\n"
