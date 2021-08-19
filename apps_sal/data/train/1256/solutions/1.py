T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    C2 = 0
    C = 0
    for i in range(N):
        if A[i] == 2:
            C2 += 1
        if A[i] > 2:
            C += 1
    ans.append(C2 * C + C * (C - 1) // 2)
for i in ans:
    print(i)
