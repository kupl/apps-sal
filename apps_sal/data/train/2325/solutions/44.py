import sys
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


S = '-' + sr()
T = '-' + sr()
Q = ir()
cnt_S = np.array([[0, 0] for _ in range(len(S))])
cnt_T = np.array([[0, 0] for _ in range(len(S))])
for (i, s) in enumerate(S[1:], 1):
    if s == 'A':
        cnt_S[i][0] = 1
    else:
        cnt_S[i][1] = 1
for (i, t) in enumerate(T[1:], 1):
    if t == 'A':
        cnt_T[i][0] = 1
    else:
        cnt_T[i][1] = 1
np.add.accumulate(cnt_S, axis=0, out=cnt_S)
np.add.accumulate(cnt_T, axis=0, out=cnt_T)
answer = []
for _ in range(Q):
    (a, b, c, d) = lr()
    num_S = cnt_S[b][0] - cnt_S[b][1] - (cnt_S[a - 1][0] - cnt_S[a - 1][1])
    num_T = cnt_T[d][0] - cnt_T[d][1] - (cnt_T[c - 1][0] - cnt_T[c - 1][1])
    if (num_S - num_T) % 3 == 0:
        answer.append('YES')
    else:
        answer.append('NO')
print('\n'.join(answer))
