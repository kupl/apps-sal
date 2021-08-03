import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    XOR = 0
    ANS = [0] * 32

    for a in A:
        XOR ^= a

        for j in range(32):
            if (1 << j) & a != 0:
                ANS[j] += 1

    if XOR == 0:
        print("DRAW")
        continue

    for i in range(31, -1, -1):
        if ANS[i] % 2 != 0:
            xx = ANS[i]
            yy = n - ANS[i]

            if xx % 4 == 3 and yy % 2 == 0:
                print("LOSE")
            else:
                print("WIN")
            break
