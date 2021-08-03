import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, m = list(map(int, input().split()))
    A = [input().strip() for i in range(n)]

    X = A[0]
    flag = 0

    for i in range(m):
        for j in range(26):
            Y = X[:i] + chr(97 + j) + X[i + 1:]

            for k in range(n):
                score = 0
                for l in range(m):
                    if Y[l] != A[k][l]:
                        score += 1
                if score <= 1:
                    True
                else:
                    break
            else:
                print(Y)
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        print(-1)
