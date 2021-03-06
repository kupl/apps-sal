import numpy as np
import sys


def findSeq(n, s, k, m, M):
    midInd = n // 2
    seqs = []
    for ind in range(midInd + 2, midInd - 3, -1):
        if ind >= n or ind < 0:
            continue
        seq = genBestSeq(n, ind, m, M, s)
        if seq is not -1 and testSeq(k, seq):
            seqs.append(list(seq))
    if len(seqs) == 0:
        return -1
    return min(seqs)


def genBestSeq(n, diffInd, m, M, s):
    arr = np.full((n,), m)
    arr[diffInd:] += 1
    s = s - np.sum(arr)
    if s < 0:
        return -1
    inc = M - m - 1
    ind = n - 1
    while ind >= 0:
        z = min(inc, s)
        arr[ind] += z
        s -= z
        ind -= 1
    if s != 0:
        return -1
    return arr


def testSeq(k, seq):
    seq = sorted(seq)
    n = len(seq)
    if n % 2 == 1:
        median = seq[n // 2]
    else:
        median = (seq[n // 2 - 1] + seq[n // 2]) / 2
    seq.pop(n % k)
    seq.pop(k - 1)
    return median != seq[(n - 2) // 2]


def __starting_point():
    nCases = int(input())
    answers = []
    for i in range(nCases):
        answers.append(findSeq(*(int(val) for val in input().split())))
        ans = answers[-1]
        if not isinstance(ans, int):
            print(*ans, sep=' ')
        else:
            print(ans)


__starting_point()
