t = int(input())
while t > 0:
    n = int(input())
    c = 0
    for i in range(1, n + 1):
        print('*' * c, end='')
        for j in range(n - i + 1, 0, -1):
            print(j, end='')
        c = c + 1
        print()
    t = t - 1
