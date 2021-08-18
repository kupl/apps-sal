
import numpy as np


N = int(input())
A, B = np.zeros(N, int), np.zeros(N, int)
for i in range(N):
    A[i], B[i] = list(map(int, input().split()))


def main():
    if (A == B).all():
        print((0))
        return

    ans = A.sum() - B[A > B].min()
    print(ans)


def __starting_point():
    main()


__starting_point()
