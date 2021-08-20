def solve(s):
    return sum([idx + 1 for (idx, digit) in enumerate(s) if int(digit) % 2 != 0])
