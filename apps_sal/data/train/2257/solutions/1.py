import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = input().strip()
    B = input().strip()

    for i in range(n):
        if A[i] > B[i]:
            print(-1)
            break
    else:
        DICT = dict()

        for i in range(n):
            a = A[i]
            b = B[i]

            if a == b:
                continue

            if a in DICT:
                DICT[a].add(b)
            else:
                DICT[a] = {b}

        ANS = 0

        for x in "abcdefghijklmnopqrst":
            if x in DICT and DICT[x] != set():
                ANS += 1
                MIN = min(DICT[x])
                if MIN in DICT:
                    DICT[MIN] = DICT[MIN] | DICT[x] - {MIN}
                else:
                    DICT[MIN] = DICT[x] - {MIN}
        print(ANS)
