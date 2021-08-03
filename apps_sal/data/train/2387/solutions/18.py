for _ in range(int(input())):

    n = int(input())

    c = 0
    while(n >= 10):
        c += n - n % 10
        n = n % 10 + n // 10
    c += n

    print(c)
