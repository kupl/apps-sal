test = int(input())
while test > 0:
    n = int(input())
    if n == 1:
        print(1)
        print(1, 1)
    else:
        print(n // 2)
        if n % 2 == 0:
            i = 1
            while i <= n:
                print(2, end=' ')
                print(i, end=' ')
                i += 1
                print(i, end=' ')
                i += 1
                print()
        else:
            i = 1
            print(3, end=' ')
            print(i, end=' ')
            i += 1
            print(i, end=' ')
            i += 1
            print(i, end=' ')
            i += 1
            print()
            while i <= n:
                print(2, end=' ')
                print(i, end=' ')
                i += 1
                print(i, end=' ')
                i += 1
                print()
    test -= 1
