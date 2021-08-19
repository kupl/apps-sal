"""
Code Chef :: December 2020 Cookoff :: Sed Passwords 
Problem Code: SEDPASS
https://www.codechef.com/COOK125A/problems/SEDPASS
"""
import sys


def solve(S):
    """Solve puzzle."""
    N = len(S)
    parity_S = 0
    qs_add = 1 << 26
    ord_a = ord('a')
    for (i, c) in enumerate(S):
        if c != '?':
            parity_S ^= 1 << ord(c) - ord_a
    good_Rs = [parity_S]
    for c in range(26):
        good_Rs.append(parity_S ^ 1 << c | qs_add)
    prefix_parities = dict()
    prefix_parities[0] = 1
    parity_R = 0
    soln = 0
    for (j, c) in enumerate(S):
        if c == '?':
            parity_R ^= qs_add
        else:
            parity_R ^= 1 << ord(c) - ord_a
        for good_R in good_Rs:
            soln += prefix_parities.get(good_R ^ parity_R, 0)
        if parity_R in prefix_parities:
            prefix_parities[parity_R] += 1
        else:
            prefix_parities[parity_R] = 1
    return soln


def main():
    """Main program."""
    test_cases = int(sys.stdin.readline())
    for _ in range(test_cases):
        S = sys.stdin.readline().strip()
        print(solve(S))


def __starting_point():
    main()


__starting_point()
