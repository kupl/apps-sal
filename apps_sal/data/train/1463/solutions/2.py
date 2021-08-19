try:
    for _ in range(int(input())):
        n = int(input())
        if n == 1:
            print(1)
            print(1, 1)
        elif n == 2:
            print(1)
            print(2, 1, 2)
        elif n == 3:
            print(1)
            print(3, 1, 2, 3)
        else:
            days = int(n / 2)
            if n % 2 == 0:
                print(days)
                for j in range(1, n + 1, 2):
                    print(2, j, j + 1)
            else:
                print(days)
                print(3, 1, 2, 3)
                for j in range(4, n + 1, 2):
                    print(2, j, j + 1)
except EOFError as e:
    print(end=' ')
