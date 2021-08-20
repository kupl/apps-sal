for _ in range(int(input())):
    n = int(input())
    x = n
    (a, b) = (65, 1)
    for _ in range(1, n + 1):
        for i in range(1, x):
            print(' ', end='')
        if _ % 2 == 1:
            for _ in range(_):
                print(chr(a), end='')
                a += 1
            print()
        else:
            for _ in range(_):
                print(b, end='')
                b += 1
            print()
        a = 65
        b = 1
        x -= 1
    print()
