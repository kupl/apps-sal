import numpy as np
N = int(input())
A = np.array(input().split(), dtype=np.int32)
B = np.array(input().split(), dtype=np.int32)


def f(t, A, B):
    power = 1 << t
    mask = (power << 1) - 1
    AA = A & mask
    BB = B & mask
    AA.sort()
    BB.sort()

    x1, x2, x3 = (np.searchsorted(BB, v - AA).sum() for v in [power, 2 * power, 3 * power])
    zero_cnt = x1 + (x3 - x2)
    return (N - zero_cnt) % 2


answer = 0
for t in range(30):
    x = f(t, A, B)
    if x == 1:
        answer += 1 << t

print(answer)
