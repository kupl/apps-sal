t = int(input())
for i in range(t):
    c = 1
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    a = set(A)
    j = 1
    while j < m and j in a:
        j += 1
    if j != m:
        print(-1)
    else:
        print(n-A.count(m))
