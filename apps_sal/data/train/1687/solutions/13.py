T = int(input())


def nb_bits(i, N):
    nb = 0
    for j in range(N):
        mask = 1 << j
        if i & mask == mask:
            nb += 1
    return nb


for t in range(T):
    (N, K) = map(int, input().strip().split(' '))
    d = {}
    for i in range(1, N + 1):
        d[i] = set()
    for i in range(2 ** N):
        nb = nb_bits(i, N)
        if nb != 0:
            d[nb].add(i)
    last = d[1].pop()
    first = last
    print(0, last)
    should_not_be = 0
    for i in range(K - 2):
        for j in range(1, N + 1):
            if len(d[j]) > 0 and j != should_not_be and (not (i == K - 3 and j == nb_bits(first, N))):
                n = d[j].pop()
                break
        print(last, n)
        should_not_be = nb_bits(last, N)
        last = n
    print(last, 0)
