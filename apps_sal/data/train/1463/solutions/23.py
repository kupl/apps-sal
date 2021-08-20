t = int(input())
while t:
    t -= 1
    n = int(input())
    if n > 1:
        print(n // 2)
    else:
        print('1')
    if n < 3:
        print(n, end=' ')
        for i in range(1, n + 1):
            print(i, end=' ')
    if n == 3:
        print('3', end=' ')
        print('1', end=' ')
        print('2', end=' ')
        print('3')
    if n > 3:
        print('3', end=' ')
        print('1', end=' ')
        print('2', end=' ')
        print('3')
        for i in range(4, n, 2):
            print('2', end=' ')
            print(i, end=' ')
            print(i + 1)
        if n % 2 == 0:
            print('1', end=' ')
            print(n)
