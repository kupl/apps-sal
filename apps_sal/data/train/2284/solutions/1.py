from collections import Counter
import sys
input = sys.stdin.readline
S = input().strip()
count = [[0] * 26 for i in range(len(S) + 1)]
c = 1
for s in S:
    for k in range(26):
        count[c][k] = count[c - 1][k]
    count[c][ord(s) - 97] += 1
    c += 1
Q = int(input())
for tests in range(Q):
    (l, r) = list(map(int, input().split()))
    if l == r:
        print('Yes')
        continue
    elif S[l - 1] != S[r - 1]:
        print('Yes')
        continue
    elif len(S) <= 4:
        print('No')
        continue
    X = [count[r][j] - count[l - 1][j] for j in range(26)]
    NZERO = 0
    for x in X:
        if x != 0:
            NZERO += 1
    if NZERO <= 2:
        print('No')
    else:
        print('Yes')
