import bisect
import sys
input = sys.stdin.readline
L = [4 ** i for i in range(30)]


def calc(x):
    fami = bisect.bisect_right(L, x) - 1
    base = (x - L[fami]) // 3
    cl = x % 3
    if cl == 1:
        return L[fami] + base
    else:
        cl1 = L[fami] + base
        ANS = 0
        for i in range(30):
            x = cl1 // L[i] % 4
            if x == 1:
                ANS += 2 * L[i]
            elif x == 2:
                ANS += 3 * L[i]
            elif x == 3:
                ANS += L[i]
        if cl == 2:
            return ANS
        else:
            return ANS ^ cl1


t = int(input())
for tests in range(t):
    print(calc(int(input())))
