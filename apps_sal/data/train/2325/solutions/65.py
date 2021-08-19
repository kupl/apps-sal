import sys
input = sys.stdin.readline
S = input()[:-1]
T = input()[:-1]
(acc0, acc1) = ([0] * (len(S) + 1), [0] * (len(S) + 1))
for i in range(len(S)):
    acc0[i + 1] = acc0[i] + (1 if S[i] == 'A' else 0)
    acc1[i + 1] = acc1[i] + (1 if S[i] == 'B' else 0)
(acc2, acc3) = ([0] * (len(T) + 1), [0] * (len(T) + 1))
for i in range(len(T)):
    acc2[i + 1] = acc2[i] + (1 if T[i] == 'A' else 0)
    acc3[i + 1] = acc3[i] + (1 if T[i] == 'B' else 0)
q = int(input())
for _ in range(q):
    (a, b, c, d) = map(int, input().split())
    A_diff = acc0[b] - acc0[a - 1] - (acc2[d] - acc2[c - 1])
    B_diff = acc1[b] - acc1[a - 1] - (acc3[d] - acc3[c - 1])
    if A_diff % 3 == B_diff % 3:
        print('YES')
    else:
        print('NO')
