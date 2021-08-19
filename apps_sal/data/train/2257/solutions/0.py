import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N = int(input())
    A = [ord(a) - 97 for a in input()]
    B = [ord(a) - 97 for a in input()]
    X = [[0] * 20 for _ in range(20)]
    for (a, b) in zip(A, B):
        X[a][b] = 1
        if a > b:
            print(-1)
            break
    else:
        ans = 0
        for i in range(20):
            for j in range(i + 1, 20):
                if X[i][j]:
                    ans += 1
                    for jj in range(j + 1, 20):
                        if X[i][jj]:
                            X[j][jj] = 1
                    break
        print(ans)
