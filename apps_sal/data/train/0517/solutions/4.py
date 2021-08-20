import sys


def get_factor(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i


(N, M) = sys.stdin.readline().strip().split(' ')[:2]
(N, M) = (int(N), int(M))
if N in (0, 1):
    print(0)
else:
    res = 2 ** N - 2
    f_ = get_factor(N)
    if f_:
        if N % f_ ** 2 == 0:
            res -= 2 ** (N // f_) - 2
        else:
            res -= 2 ** (N // f_) - 2 + 2 ** f_ - 2
    print(res % M)
