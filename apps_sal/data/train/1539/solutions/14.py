
import sys
import time
import math


testCases = int(sys.stdin.readline())

for i in range(testCases):
    count = 0
    jewels = {}
    jewelsLine = sys.stdin.readline().strip()
    for char in jewelsLine:
        if char in jewels:
            jewels[char] += 1
        else:
            jewels[char] = 1
    stonesLine = sys.stdin.readline().strip()
    for stone in stonesLine:
        if stone in jewels:
            if jewels[stone] > 0:
                count += 1
    sys.stdout.write("%d\n" % count)
