import sys
sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline
n = int(input())
a = [int(i) for i in readline().split()]


def zeta_transform(a, n):
    b = [[i, 0] for i in a]
    for i in range(n):
        I = 1 << i
        for j in range(1 << n):
            if not j & I:
                if b[j][0] > b[j ^ I][0]:
                    (b[j ^ I][0], b[j ^ I][1]) = (b[j][0], b[j ^ I][0])
                    if b[j][1] > b[j ^ I][1]:
                        b[j ^ I][1] = b[j][1]
                elif b[j][0] > b[j ^ I][1]:
                    b[j ^ I][1] = b[j][0]
    return b


za = zeta_transform(a[:], n)
for (i, zi) in enumerate(za):
    if not i:
        ans = 0
    else:
        (i1, i2) = za[i]
        ans = max(ans, i1 + i2)
        print(ans)
