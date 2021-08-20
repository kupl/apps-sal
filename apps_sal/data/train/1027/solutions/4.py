for _ in range(int(input())):
    (n, p) = map(int, input().split())
    if p >= n:
        if n == 1 or n == 2:
            print('impossible')
        else:
            print('a' + 'b' * (n - 2) + 'a')
    elif n % p != 0:
        print('impossible')
    elif p == 1 or p == 2:
        print('impossible')
    else:
        s = 'a' + 'b' * (p - 2) + 'a'
        print(s * (n // p))
