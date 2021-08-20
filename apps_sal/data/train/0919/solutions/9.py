"""
Code Chef :: December 2020 Lunchtime :: Even Sequence Problem Code: EVSTR
https://www.codechef.com/LTIME91B/problems/EVSTR
"""
import sys
from math import inf


def solve(A):
    prev = 0
    count = 0
    ops = 0
    for (i, a) in enumerate(A):
        if a == prev:
            count += 1
        elif count % 2:
            if i + 1 < len(A) and A[i + 1] == prev:
                ops += 1
            else:
                ops += 1
                count = 1
                prev = a
        else:
            count = 1
            prev = a
    if count % 2:
        ops += 1
    return ops


def main():
    """Main program."""
    sys.setrecursionlimit(pow(10, 9))
    test_cases = int(sys.stdin.readline())
    for _ in range(test_cases):
        N = int(sys.stdin.readline())
        A = [int(i) for i in sys.stdin.readline().split()]
        soln = solve(A)
        print(soln)


def __starting_point():
    main()


__starting_point()
