t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = []
    print(0)
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == i:
                print(i, end='')
            else:
                print('*', end='')
        print()
