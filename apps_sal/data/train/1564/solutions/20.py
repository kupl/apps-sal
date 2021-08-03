

import fractions
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")


def calc(s):
    codes = set()
    for i in range(1, len(s)):
        ch1 = s[i - 1]
        ch2 = s[i]
        codes.add((ch1, ch2))
    return len(codes)


T = int(f.readline().strip())

for case_id in range(1, T + 1):
    s = f.readline().strip()

    r = calc(s)

    print(r)
