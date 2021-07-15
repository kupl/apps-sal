import itertools

# Walk through s from left to right. If the current digit is odd,
# It can create odd substrings with every previous digit.
# The total number of substrings that can be made at each digit
# location is (1 + digit_index)
def solve(s):
    return sum([i + 1 for i, d in enumerate(s) if d in '13579'])
