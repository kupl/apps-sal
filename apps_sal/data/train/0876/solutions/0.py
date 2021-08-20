t = int(input())
for t1 in range(t):
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    mx = max(a)
    mn = min(a)
    if mx - mn < x:
        print('YES')
    else:
        print('NO')
