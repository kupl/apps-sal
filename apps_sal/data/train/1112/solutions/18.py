for _ in range(int(input())):
    n = int(input())
    x = 1
    for _ in range(1, n + 1):
        for __ in range(n - _ + 1, 0, -1):
            print(x, end='')
            x += 1
        print()
    print()
