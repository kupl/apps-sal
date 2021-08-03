# supports any number greater than 1000 and also negative number

from collections import defaultdict

d = defaultdict(lambda: 1e2)


def parts(n, li):
    if not n:
        for b in range(2 ** (len(li) - 1)):
            bits = bin(b)[2:].zfill(len(li))
            sum_ = sum(int(k) * [1, -1][int(l)] for k, l in zip(li, bits))
            d[sum_] = min(d[sum_], len(bits) - 1)
        return
    for i in range(1, len(n) + 1):
        li.append(n[:i])
        parts(n[i:], li)
        li.pop()


parts('123456789', [])


def operator_insertor(n):
    return d[n] if d[n] < 9 else None


operator_insertor(1234656)
operator_insertor(1234550)
operator_insertor(1234584)
operator_insertor(-4453)
operator_insertor(-55555)
