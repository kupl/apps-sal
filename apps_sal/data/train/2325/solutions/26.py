from itertools import accumulate
import sys
input = sys.stdin.readline

S = input()
T = input()
cntS = [1 if S[i] == 'A' else -1 for i in range(len(S))]
cntT = [1 if T[i] == 'A' else -1 for i in range(len(T))]
cumS = list(accumulate([0] + cntS))
cumT = list(accumulate([0] + cntT))
q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    if (cumS[b] - cumS[a-1]) % 3 == (cumT[d] - cumT[c-1]) % 3:
        print('YES')
    else:
        print('NO')
