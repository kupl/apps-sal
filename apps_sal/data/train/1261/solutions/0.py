

import fractions
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")


def calc(N, M):
    if M != N:
        return [(-1, -1)]
    r = [(i + 1, ((i + 1) % N) + 1) for i in range(N)]
    return r


T = int(f.readline().strip())

for case_id in range(1, T + 1):
    N, M = list(map(int, f.readline().strip().split()))

    rr = calc(N, M)

    for a, b in rr:
        print(a, b)
