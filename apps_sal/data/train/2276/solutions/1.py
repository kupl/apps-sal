import sys
input = sys.stdin.readline

t = int(input())
for testcases in range(t):
    n, m = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(n)]

    B = []
    for j in range(m):
        B.append([A[i][j] for i in range(n)])

    B.sort(key=lambda x: max(x), reverse=True)

    B = B[:n]

    LEN = len(B)

    if LEN == 1:
        print(sum(B[0]))

    elif LEN == 2:
        ANS = 0
        for i in range(n):
            A = 0
            for k in range(n):
                A += max(B[0][k], B[1][(i + k) % n])

            ANS = max(ANS, A)

        print(ANS)

    elif LEN == 3:

        ANS = 0
        for i in range(n):
            for j in range(n):

                A = 0
                for k in range(n):
                    A += max(B[0][k], B[1][(i + k) % n], B[2][(j + k) % n])

                ANS = max(ANS, A)

        print(ANS)

    elif LEN == 4:

        ANS = 0
        for i in range(n):
            for j in range(n):
                for l in range(n):

                    A = 0
                    for k in range(n):
                        A += max(B[0][k], B[1][(i + k) % n], B[2][(j + k) % n], B[3][(l + k) % n])

                    ANS = max(ANS, A)

        print(ANS)
