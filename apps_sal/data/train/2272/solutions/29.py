import sys
import bisect
input = sys.stdin.readline


def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    res = 0
    p = 0
    for i in range(1, 30):
        p += 1 << i - 1
        A = []
        B = []
        for j in range(n):
            A.append(a[j] & p)
            B.append(b[j] & p)
        A.sort()
        B.sort()
        cnt = 0
        q2 = p + 1
        q1 = q2 >> 1
        q3 = q2 << 1
        (k1, k2, k3, k4) = (0, 0, 0, 0)
        for j in range(n - 1, -1, -1):
            while k1 < n and A[j] + B[k1] < q1:
                k1 += 1
            while k2 < n and A[j] + B[k2] < q2:
                k2 += 1
            while k3 < n and A[j] + B[k3] < 3 * q1:
                k3 += 1
            while k4 < n and A[j] + B[k4] < q3:
                k4 += 1
            cnt += k4 + k2 - k1 - k3
        if cnt % 2 != 0:
            res += 1 << i - 1
    print(res)


def __starting_point():
    main()


__starting_point()
