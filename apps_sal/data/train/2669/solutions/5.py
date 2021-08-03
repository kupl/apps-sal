from functools import reduce


def convergence(n):
    print(n)
    t, r = [1], [n]
    def f(x): return x + reduce(lambda x, y: x * y, (int(i) for i in str(x) if i != '0'))
    while r[-1] not in t:
        for _ in range(25):
            t += [f(t[-1])]
        r += [f(r[-1])]
    return len(r) - 1
