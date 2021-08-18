import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(N + 1)]
    fc = 0
    flag = 0
    for i in A:
        if (B[i] != 1):
            fc = fc + 1
            B[i] = B[i] + 1
        else:
            flag = flag + 1
    if (flag % 2 == 0):
        print(fc)
    else:
        print(max(fc - 1, 1))
