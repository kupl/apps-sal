__author__ = 'Hacktivist'

from sys import stdin

testCases = int(stdin.readline().strip())
for test in range(testCases):
 s = str(stdin.readline().strip())
 print(int(s[::-1]))
