import sys
input = sys.stdin.readline
testcase = int(input())
e = 0.0000005


def check(m):
    curr = 0
    for i in range(n):
        if curr <= a[i]:
            curr = a[i] + m
        elif curr <= (a[i] + d):
            curr = curr + m
        else:
            return False
    return True


def bs(l, h):
    m = (l + h) / 2
    if check(m):
        if (m + e) <= h and check(m + e):
            return bs(m + e, h)
        else:
            return m
    else:
        return bs(l, m - e)


for _ in range(testcase):
    n, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    print(bs(0, max(a) + d))
