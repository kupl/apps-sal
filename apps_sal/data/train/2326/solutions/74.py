import sys
from bisect import bisect_left, bisect_right, insort


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


' \n左側で自分より小さい数字との差\n右側で自分より大きい数字の数\n石数最大の山で右の物から取り除く\n'
N = ir()
A = lr()
A = [(x, i + 1) for (i, x) in enumerate(A)] + [(0, 0)]
A.sort(reverse=True)
answer = [0] * (N + 1)
mi = 10 ** 10
mi_index = 10 ** 10
for (i, (x, j)) in enumerate(A[:-1]):
    diff = A[i][0] - A[i + 1][0]
    index = A[i][1]
    if index < mi_index:
        mi_index = index
    answer[mi_index] += diff * (i + 1)
print('\n'.join(map(str, answer[1:])))
