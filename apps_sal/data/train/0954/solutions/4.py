for _ in range(int(input())):
    k = int(input())
    a = k * (k + 1)
    a = a / 2
    a = a ** 2
    print(int(2 * a - k ** 3))
