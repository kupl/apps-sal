for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(n // 2)
        for i in range(1, n + 1, 2):
            print(2, i, i + 1)
    else:
        if n == 1:
            print(1)
            print(1, 1)
        elif n >= 3:
            print(n // 2)
            print(3, 1, 2, 3)
            for i in range(4, n + 1, 2):
                print(2, i, i + 1)
