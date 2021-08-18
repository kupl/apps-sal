from itertools import accumulate


def solve(A):
    def keep_max_2(i, j, k):
        if i == k or j == k:
            return i, j
        if A[j] > A[k]:
            return i, j
        elif A[i] > A[k]:
            return i, k
        else:
            return k, i
    n = len(A)
    dp0 = [0] * n
    dp1 = [0] * n

    small = min((a, i) for i, a in enumerate(A))[1]

    for i in range(1, n):
        x, y = (i, 0) if A[i] > A[0] else (0, i)
        for d in range(n.bit_length() - 1):
            j = i ^ (1 << d)
            if j > i:
                continue
            x, y = keep_max_2(x, y, dp0[j])
            x, y = keep_max_2(x, y, dp1[j])
        dp0[i] = x
        dp1[i] = y
    return accumulate((A[dp0[i]] + A[dp1[i]] for i in range(1, n)), max)


def __starting_point():
    n = int(input())
    A = tuple(map(int, input().split()))
    print(*solve(A), sep='\n')


__starting_point()
