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
    qs_add = (1 << 26)
    ord_a = ord('a')
    for i, c in enumerate(S):
        if c != '?':
            parity_S ^= (1 << (ord(c) - ord_a))

    # The 27 good bitsets.
    # The first is even parity ?s (26th bit = 0) and parity_S
    good_Rs = [parity_S]
    for c in range(26):
        # The rest are odd parity ?s (26th bit) and parity_S with one
        # character, c, with the opposite parity.
        good_Rs.append((parity_S ^ (1 << c)) | qs_add)

    # A substring S[i:j] has a parity of S[:j] ^ S[:i].
    # a ^ b = c implies a ^ c = b.
    # If S[:j] ^ a good_Rs = some S[:i] then S[i:j] is a good substring.
    # So if we keep track of the S[:i] that we have already seen and 
    # at each j check each good_Rs to see if it matches previous S[:j]s
    # that we have cached.  Note: a subtring parity may occur more than once.
    prefix_parities = dict()
    prefix_parities[0] = 1  # Be sure to add an empty S[:i].

    parity_R = 0
    soln = 0
    for j, c in enumerate(S):
        if c == "?":
            parity_R ^= qs_add
        else:
            parity_R ^= (1 << (ord(c) - ord_a))

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
