for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    if n % m % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
