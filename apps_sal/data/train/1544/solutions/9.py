for _ in range(int(input())):
    n = int(input())
    print('*')
    for i in range(2, n):
        print('*' + ' ' * (i - 2) + '*')
    if n > 1:
        print(n * '*')
