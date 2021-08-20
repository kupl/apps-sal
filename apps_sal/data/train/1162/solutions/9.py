import sys
import time
import math
testCases = int(sys.stdin.readline())
for i in range(testCases):
    fours = 0
    N = int(sys.stdin.readline())
    fours = N / 7 * 7
    n = int(N)
    while fours >= 0:
        if (n - fours) % 4 == 0:
            break
        else:
            fours -= 7
    if fours >= 0:
        sys.stdout.write('%d\n' % fours)
    else:
        sys.stdout.write('-1\n')
