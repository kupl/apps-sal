for _ in range(eval(input())):
    (n, m) = list(map(int, input().split()))
    x = n % m
    if x % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
