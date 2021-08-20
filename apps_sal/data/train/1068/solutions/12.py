for _ in range(int(input())):
    (x, y) = list(map(int, input().split()))
    print('NO' if x * y % 2 else 'YES')
