import sys


def solve():
    a = sys.stdin.readline()
    b = sys.stdin.readline()

    def arrange(a, A):
        for i in a:
            if '0' <= i <= '3':
                A[0] += 1
            elif i == '4':
                A[1] += 1
            elif i == '7':
                A[2] += 1
            elif '5' <= i <= '6':
                A[3] += 1
    (A, B) = ([0] * 5, [0] * 5)
    arrange(a, A)
    arrange(b, B)
    ret = ''
    ret = (min(A[2], B[3]) + min(B[2], A[3])) * '7'
    (A[2], B[2]) = (max(0, A[2] - B[3]), max(0, B[2] - A[3]))
    t = min(A[1] + B[1], A[1] + A[0], B[1] + B[0])
    A[0] = A[1] + A[0] - t
    B[0] = B[1] + B[0] - t
    ret = ret + (min(A[2], B[0]) + min(B[2], A[0])) * '7'
    (A[2], B[2]) = (max(0, A[2] - B[0]), max(0, B[2] - A[0]))
    ret = ret + (min(t, A[2]) + min(t, B[2])) * '7'
    k = min(max(0, t - A[2]), max(0, t - B[2]))
    (A[2], B[2]) = (max(0, A[2] - t), max(0, B[2] - t))
    ret = ret + min(A[2], B[2]) * '7' + k * '4'
    print(ret)
    return


t = int(input())
for i in range(t):
    solve()
