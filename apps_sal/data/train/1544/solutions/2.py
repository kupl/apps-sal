t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        if i == n - 1:
            print('*' * (i + 1))
        elif i == 0:
            print('*')
        else:
            print('*' + ' ' * (i + 1 - 2) + '*')
