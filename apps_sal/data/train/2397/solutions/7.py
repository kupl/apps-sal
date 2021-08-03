import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, m = list(map(int, input().split()))
    A = sorted([int(input().strip(), 2) for i in range(n)])
    A += [1 << 63]

    ind = (2**m - n - 1) // 2

    indskip = 0
    ANS = 0

    # print(A)

    while True:
        # print(ANS,ind,indskip)
        if A[indskip] == ANS:
            ANS += 1
            indskip += 1
            continue
        if A[indskip] - ANS <= ind:
            ind -= A[indskip] - ANS
            ANS = A[indskip] + 1
            indskip += 1
        else:
            ANS += ind
            break

    print(bin(ANS)[2:].zfill(m))
