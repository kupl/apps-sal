for tc in range(int(input().strip())):
    (n, m) = list(map(int, input().split()))
    r = n % m
    if r & 1 == 0:
        print('EVEN')
    else:
        print('ODD')
