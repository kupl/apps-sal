

import itertools
import sys
inp = sys.stdin
out = sys.stdout
cases = int(inp.readline())


def lucky_number_4(num):
    if num < 4:
        return -1
    if num == 4:
        return 0
    if num < 7:
        return -1
    fours = num - (num % 7)
    for i in range(fours, 0, -7):
        if (num - i) % 4 == 0:
            return i
    return -1


outputs = []
for case in range(1, cases + 1):
    num = int(inp.readline())
    fours = lucky_number_4(num)

    out.write(str(fours) + "\n")
