import sys
input = sys.stdin.readline


def construct(A, count, MAX):
    B = []
    NMAX = 0
    for l, r in A:
        if r - l + 1 == MAX:
            ANS[(r + l) // 2] = count
            count += 1

            if l <= (r + l) // 2 - 1:
                NMAX = max(NMAX, (r + l) // 2 - l)
                B.append((l, (r + l) // 2 - 1))
            if r >= (r + l) // 2 + 1:
                NMAX = max(NMAX, r - (r + l) // 2)
                B.append(((r + l) // 2 + 1, r))
        else:
            NMAX = max(NMAX, r - l + 1)
            B.append((l, r))
    if NMAX != 0:
        construct(B, count, NMAX)


t = int(input())
for tests in range(t):
    n = int(input())
    ANS = [0] * n
    construct([(0, n - 1)], 1, n)
    print(*ANS)
