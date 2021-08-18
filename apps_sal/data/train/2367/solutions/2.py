from collections import Counter
import sys
input = sys.stdin.readline

q = int(input())


for testcases in range(q):
    n = int(input())
    S = input().strip()
    T = input().strip()

    CS = Counter(S)
    CT = Counter(T)

    if CS != CT:
        print("NO")
        continue

    if max(CS.values()) >= 2:
        print("YES")
        continue

    W = [0] * 26
    SA = 0

    for s in S:
        SA += sum(W[ord(s) - 97:])
        W[ord(s) - 97] += 1

    W = [0] * 26
    TA = 0

    for s in T:
        TA += sum(W[ord(s) - 97:])
        W[ord(s) - 97] += 1

    if (SA + TA) % 2 == 0:
        print("YES")
    else:
        print("NO")
