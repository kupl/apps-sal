for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n, 0, -1):
        a.append(i)
    for i in range(1, n + 1):
        print(' ' * (n + 1 - i), end='')
        for j in a[0:i]:
            print(j, end='')
        print('')
    a.append(0)
    for i in a:
        print(i, end='')
    a.pop()
    print('')
    for i in range(1, n + 1):
        print(' ' * i, end='')
        for j in a[0:n - i + 1]:
            print(j, end='')
        print('')
