from itertools import accumulate


def zeta(data, merge):
    """
    （この関数はdataを上書きします）
    Mはモノイド
    data: 2^n -> M
    output: 2^n -> M
    merge: M -> M

    ouput[i] = sum(data[j] for j in range(2^n) if i|j == i)
    """
    n = len(data)
    i = 1
    while i < n:
        j = i
        while j < n:
            data[j] = merge(data[j], data[j & ~i])
            j = j + 1 | i
        i <<= 1
    return data


def solve(A):

    def merge(x, y):
        return sorted(x + y)[-2:]
    data = [[a] for a in A]
    zeta(data, merge)
    return accumulate((sum(x) for x in data[1:]), max)


def __starting_point():
    n = int(input())
    A = tuple(map(int, input().split()))
    print(*solve(A), sep='\n')


__starting_point()
