for _ in range(int(input())):
    (m, n) = map(int, input().split())
    print('NO' if m * n % 2 else 'YES')
