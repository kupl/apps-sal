# LuckyNumbers.py
# Code Chef Problem: Lucky Lucky Number
#   http://www.codechef.com/MAY12/problems/CHEFLUCK
#   May Long Challenge 2012
# Benjamin Johnson
# May 5 2012 9:35
# Lessons Learned: Math review: 0 is divisible by all numbers

import sys,time,math

#Use the test file when testing
#testInputFile = open("test.in","r")

#Get input here
testCases = int(sys.stdin.readline())
#testCases = int(testInputFile.readline())

for i in range(testCases):
    fours = 0
    #N = int(testInputFile.readline())
    N = int(sys.stdin.readline())
    fours = (N/7)*7 #Will not be N
    n = int(N)
    while fours >= 0:
        # Check to see if N-fours is divisible by 4
        if (n-fours)%4 == 0:
            break;
        else:
            fours -= 7
    if fours >= 0:
        sys.stdout.write("%d\n"%fours)
    else:
        sys.stdout.write("-1\n")
#testInputFile.close()

