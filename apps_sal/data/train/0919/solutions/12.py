"""
Code Chef :: December 2020 Lunchtime :: Even Sequence Problem Code: EVSTR
https://www.codechef.com/LTIME91B/problems/EVSTR
"""
import sys
from math import inf


def solve(i, prev, cnt, ops, A):
    # Base Case
    if i >= len(A):
        if cnt % 2 == 0:
            return ops
        else:
            return inf

    result = inf
    if A[i] == prev:
        result = min(result, solve(i + 1, prev, cnt + 1, ops, A))
    else:
        if cnt % 2:
            # If cnt is odd, we can
            # (1) Fix it and add current.  It will cost on op to fix.
            result = min(result, solve(i + 1, A[i], 1, ops + 1, A))
            # (2) Not fix it and delete current.
            result = min(result, solve(i + 1, prev, cnt, ops + 1, A))
        else:
            # If cnt is even, we can
            # (1) Delete current
            result = min(result, solve(i + 1, prev, cnt, ops + 1, A))
            # (2) Add current
            result = min(result, solve(i + 1, A[i], 1, ops, A))
    return result


def main():
    """Main program."""
    sys.setrecursionlimit(pow(10, 9))
    test_cases = int(sys.stdin.readline())
    for _ in range(test_cases):
        N = int(sys.stdin.readline())
        A = [int(i) for i in sys.stdin.readline().split()]
        soln = solve(0, 0, 0, 0, A)
        print(soln)


def __starting_point():
    main()


__starting_point()
