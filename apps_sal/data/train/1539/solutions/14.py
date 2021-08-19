# Jewels.py
# Code Chef Problem: Jewels and Stones
#   http://www.codechef.com/MAY12/problems/STONES
#   May Long Challenge 2012
# Benjamin Johnson
# May 4 2012
# Lessons Learned:

import sys
import time
import math

# Use the test file when testing
#testInputFile = open("test.in","r")

# Get input here
testCases = int(sys.stdin.readline())
#testCases = int(testInputFile.readline())

for i in range(testCases):
    count = 0
    jewels = {}
    #jewelsLine = testInputFile.readline().strip()
    jewelsLine = sys.stdin.readline().strip()
    for char in jewelsLine:
        if char in jewels:
            jewels[char] += 1
        else:
            jewels[char] = 1
    #stonesLine = testInputFile.readline().strip()
    stonesLine = sys.stdin.readline().strip()
    for stone in stonesLine:
        if stone in jewels:
            if jewels[stone] > 0:
                #jewels[stone] -= 1
                count += 1
    sys.stdout.write("%d\n" % count)

# testInputFile.close()
