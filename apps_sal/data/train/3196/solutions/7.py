from math import sqrt


def triangular_range(start, stop):

    def get_n(sum):
        a = int(round((sqrt(8 * sum) - 1) / 2, 0))
        return a
    return {n: int(n * (n + 1) / 2) for n in range(get_n(start), get_n(stop) + 1) if start <= int(n * (n + 1) / 2) <= stop}
