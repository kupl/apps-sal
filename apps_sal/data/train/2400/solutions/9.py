import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    ANS = [-1] * n
    ANS[0] = 1
    if min(A) == max(A):
        print(1)
        print(*[1] * n)
        continue
    if n % 2 == 1:
        flag = 0
    else:
        flag = 1
    for i in range(1, n):
        if flag == 0:
            if A[i] == A[i - 1]:
                ANS[i] = ANS[i - 1]
                flag = 1
            else:
                ANS[i] = 3 - ANS[i - 1]
        else:
            ANS[i] = 3 - ANS[i - 1]
    if flag == 0 and A[i] != A[0]:
        ANS[n - 1] = 3
    print(max(ANS))
    print(*ANS)
