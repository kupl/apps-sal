import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print("NO")
else:
    print("YES")
    ANS = [0] * (2 * n)
    for i in range(n):
        if i % 2 == 0:
            ANS[i] = (i + 1) * 2 - 1
            ANS[i + n] = (i + 1) * 2

        else:
            ANS[i] = (i + 1) * 2
            ANS[i + n] = (i + 1) * 2 - 1

    print(*ANS)
