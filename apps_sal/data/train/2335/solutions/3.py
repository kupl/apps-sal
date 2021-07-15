import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(a) - 1 for a in input().split()]
    D = {a: i for i, a in enumerate(A)}
    X = [0] * N + [1]
    pre = N - 1
    for k in range(N):
        i = D[k]
        if X[pre + 1] or i == pre + 1:
            pre = i
            X[pre] = 1
        else:
            print("No")
            break
    else:
        print("Yes")

