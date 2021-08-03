import bisect
import sys
input = sys.stdin.readline


def calc():
    n = int(input())
    arr = list(map(int, input().split()))
    l = int(input())
    pos = 0
    dbl = [[0] * (n + 1)]
    for i in range(n):
        dbl[0][i + 1] = bisect.bisect_right(arr, arr[i] + l)
    for _ in range(n.bit_length() - 1):
        tmp = [0] * (n + 1)
        for i in range(n + 1):
            tmp[i] = dbl[-1][dbl[-1][i]]
        dbl.append(tmp)
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        l = 0
        r = b - a + 1
        while r - l != 1:
            mid = (l + r) // 2
            tmp = a
            for i in range(mid.bit_length()):
                if mid & (1 << i):
                    tmp = dbl[i][tmp]
            if tmp >= b:
                r = mid
            else:
                l = mid
        print(r)


calc()
