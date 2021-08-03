from itertools import chain, cycle, islice


def pattern(n):
    w = 2 * n - 1

    def f():
        for i in chain(range(1, n + 1), range(n - 1, 0, -1)):
            xs = ''.join(islice(cycle('1234567890'), i))
            yield (xs + xs[-2::-1]).center(w)
    return '\n'.join(f())
