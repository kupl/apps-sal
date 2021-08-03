from itertools import cycle, chain


def printhex(b):
    for x in b:
        st = ' '.join(map(str, x))
        print(f'{st:^{2*len(b)-1}}')


def d1sum(b, n, l):
    d1_sum = []
    for i in range(l):
        dsum = 0
        if i + n <= l:
            k = 1
            for x in range(n + i):
                if x < n:
                    dsum += b[x][i]
                else:
                    dsum += b[x][i - k]
                    k += 1
        else:
            k = 1
            for x in range(i - n + 1, l):
                if x < n:
                    dsum += b[x][i]
                else:
                    dsum += b[x][i - k]
                    k += 1
        d1_sum.append(dsum)
    return d1_sum


def d2sum(b, n, l):
    d2_sum = []
    for i in range(l):
        dsum = 0
        if i + n <= l:
            k = 1
            for x in range(n + i):
                if x < n:
                    dsum += b[x][-1 - i]
                else:
                    dsum += b[x][-1 - i + k]
                    k += 1
        else:
            k = 1
            for x in range(i - n + 1, l):
                if x < n:
                    dsum += b[x][-1 - i]
                else:
                    dsum += b[x][-1 - i + k]
                    k += 1
        d2_sum.append(dsum)
    return d2_sum


def max_hexagon_beam(n: int, seq: tuple):
    print((n, seq))
    l = 2 * n - 1
    b = []
    hb_sum = []
    itr = cycle(seq)
    for i in range(l):
        tmp = []
        if i + n <= l:
            k = i + n
        else:
            k = l - (i - n + 1)
        for j in range(k):
            tmp.append(next(itr))
        b.append(tmp)
        hb_sum.append(sum(tmp))

    # printhex(b)
    d1_sum = d1sum(b, n, l)
    d2_sum = d2sum(b, n, l)
    return(max(chain(hb_sum, d1_sum, d2_sum)))
