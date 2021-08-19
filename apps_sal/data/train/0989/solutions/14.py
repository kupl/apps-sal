for _ in range(int(input())):
    (c, p, k) = list(map(int, input().split()))
    a = c + p
    c = a // k
    if c % 2 == 0:
        print('Chef')
    else:
        print('Paja')
