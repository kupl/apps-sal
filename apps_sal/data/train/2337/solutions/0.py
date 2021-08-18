from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
for testcases in range(t):
    n = int(input())
    P = list(map(int, input().split()))
    C = Counter(P)
    PLIST = sorted(set(P), reverse=True)

    g = C[PLIST[0]]
    s = 0
    b = 0

    sflag = 1

    for i in PLIST[1:]:

        if sflag:
            if s <= g:
                s += C[i]
            else:
                sflag = 0
                bflag = 1
                b += C[i]

        elif bflag:
            if b <= g:
                b += C[i]
            elif g + s + b + C[i] <= n // 2:
                b += C[i]
            else:
                break

    if g + s + b <= n // 2:
        print(g, s, b)
    else:
        print(0, 0, 0)
