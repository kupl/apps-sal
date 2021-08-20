import sys
from itertools import chain


def solve(N: int, A: 'List[int]'):
    total = 0
    for a in A:
        total ^= a
    return [total ^ a for a in A]


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    ans = solve(N, A)
    print(' '.join([str(a) for a in ans]))


def __starting_point():
    main()


__starting_point()
