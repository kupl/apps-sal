for _ in range(int(input())):
    (n, k) = map(int, input().split())
    if n % k ** 2 == 0:
        print('NO')
    else:
        print('YES')
