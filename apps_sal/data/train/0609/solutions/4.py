def solve(n, k, q):
    leftq = 0
    for i in range(n):
        leftq = leftq + q[i]
        if leftq < k:
            return i + 1
        leftq = leftq - k
    return n + leftq // k + 1


t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    print(solve(n, k, queries))
