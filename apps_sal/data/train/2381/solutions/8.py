from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    S = input().strip()

    NOW = 0
    ANS = 0
    for s in S:
        if s == "L":
            NOW += 1
        else:
            ANS = max(ANS, NOW)
            NOW = 0
    ANS = max(ANS, NOW)
    print(ANS + 1)
