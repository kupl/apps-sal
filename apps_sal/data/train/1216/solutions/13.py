for _ in range(int(input())):
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    if max(l) >= k:
        print('YES')
    else:
        print('NO')
