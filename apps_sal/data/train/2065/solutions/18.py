#!/usr/bin/env python3

def solve(n, seq):
    found = 0
    res = 0
    for s in seq:
        if s[1] == 1:
            found = 1
            while len(s) > found and s[found] == found:
                found += 1
            found -= 1
            rest = s[0] - found
            res += rest
        else:
            res += s[0]-1
    return res + n - found


def __starting_point():
    n, k = list(map(int, input().split()))
    seq = [list(map(int, input().split())) for _ in range(k)]
    print(solve(n, seq))

__starting_point()
