from itertools import cycle


def spinning_rings(inMax, outMax):
    (inc, outc) = (cycle([0] + list(range(1, inMax + 1))[::-1]), cycle(range(outMax + 1)))
    (a, b, count) = (next(inc), next(outc), 0)
    while True:
        (a, b, count) = (next(inc), next(outc), count + 1)
        if a == b:
            return count
