t = int(input())
while t:
    n = int(input())
    for i in range(n):
        for j in range(i, 0, -1):
            print('*', end='')
        for j in range(n - i, 0, -1):
            print(j, end='')
        print()
    t -= 1
