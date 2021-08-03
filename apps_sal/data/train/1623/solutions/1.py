from fractions import Fraction as f


def bernoulli_number(n):
    if n == 1:
        return f(-1, 2)
    if n % 2 == 1:
        return 0
    с = [i for i in zip(range(n + 2), consider())]
    с = [b for _, b in с]
    return с[n]


def consider():
    k, t = [], 0
    while True:
        k.append(f(1, t + 1))
        for j in range(t, 0, -1):
            k[j - 1] = j * (k[j - 1] - k[j])
        yield k[0]
        t += 1
