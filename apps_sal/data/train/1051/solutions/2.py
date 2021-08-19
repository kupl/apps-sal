for u in range(int(input().strip())):
    n = int(input().strip())
    for i in range(n + 1):
        for space in range(0, i + 1):
            if space == i:
                print(i, end='')
            else:
                print('*', end='')
        print()
