import sys
input = sys.stdin.readline


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


def main():
    mod = 10**9 + 7
    N = I()
    ans = 0
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = MI()

    if A == B:
        print((0))

    else:
        ans = sum(A)
        m = 10**10
        for i in range(N):
            if A[i] > B[i]:
                m = min(m, B[i])

        print((ans - m))


main()
