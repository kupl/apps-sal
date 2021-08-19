t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    f = n // k
    if f % k == 0:
        print('NO')
    else:
        print('YES')
