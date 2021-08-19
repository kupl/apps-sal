#!/bin/python3

import sys
from collections import Counter


def __starting_point():
    s = input().strip()
    best = Counter(s)
    sortit = sorted(list(best.items()), key=lambda x: (-x[1], x[0]))[:3]

    print(("\n".join(x[0] + " " + str(x[1]) for x in sortit)))


__starting_point()
