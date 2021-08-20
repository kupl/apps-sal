import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
P = 10 ** 9 + 7
for _ in range(T):
    (N, b) = list(map(int, input().split()))
    A = sorted([int(a) for a in input().split()])
    if b == 1:
        print(N % 2)
        continue
    a = A.pop()
    pre = a
    s = 1
    ans = pow(b, a, P)
    while A:
        a = A.pop()
        s *= b ** min(pre - a, 30)
        if s >= len(A) + 5:
            ans -= pow(b, a, P)
            if ans < 0:
                ans += P
            while A:
                a = A.pop()
                ans -= pow(b, a, P)
                if ans < 0:
                    ans += P
            print(ans)
            break
        if s:
            s -= 1
            ans -= pow(b, a, P)
            if ans < 0:
                ans += P
            pre = a
        else:
            s = 1
            ans = -ans
            if ans < 0:
                ans += P
            ans += pow(b, a, P)
            if ans >= P:
                ans -= P
            pre = a
    else:
        print(ans)
