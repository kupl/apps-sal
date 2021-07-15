for _ in range(int(input())):
    n = int(input())
    print('*')
    for i in range(1, n // 2):
        print(' ' * (i) + '*')
    for i in range(n // 2, 0, -1):
        print(' ' * (i) + '*')
    if n > 1:
        print('*')

