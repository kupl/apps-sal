for _ in range(int(input())):
    n = int(input())
    s = ''
    for i in range(1, n + 1):
        s += str(i)
    for i in range(n, 0, -1):
        if i % 2 == 0:
            for j in range(i, 0, -1):
                print(j, end='')
        else:
            for j in range(1, i + 1):
                print(j, end='')
        print()
