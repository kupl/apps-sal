def solve(A, n):
    A.sort()
    res = 0
    for i in range(1, n):
        res = res + A[i] * A[0]
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print(solve(A, n))
