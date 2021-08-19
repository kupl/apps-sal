t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    rest = n // k
    if rest % k == 0:
        print('NO')
    else:
        print('YES')
