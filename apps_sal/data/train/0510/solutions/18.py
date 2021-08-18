from bisect import bisect_left, insort_left
import sys
input = sys.stdin.readline
OFS = ord('a')
_ = input()
S = list(input()[:-1])

D = [[] for _ in [0] * 26]
for i, s in enumerate(S):
    D[ord(s) - OFS].append(i)

for _ in [0] * int(input()):
    Q = input()[:-1].split()
    if Q[0] == '1':
        i, c = int(Q[1]) - 1, Q[2]

        if S[i] != c:
            s = ord(S[i]) - OFS
            D[s].pop(bisect_left(D[s], i))
            insort_left(D[ord(c) - OFS], i)
            S[i] = c

    else:
        l, r = int(Q[1]) - 1, int(Q[2]) - 1

        cnt = 0
        for L in D:
            i = bisect_left(L, l)
            if i < len(L) and L[i] <= r:
                cnt += 1

        print(cnt)
