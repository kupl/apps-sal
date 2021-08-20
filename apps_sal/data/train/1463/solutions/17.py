t = int(input())
while t > 0:
    t = t - 1
    n = int(input())
    if n == 1:
        print(1)
        print(1, 1)
    else:
        print(n // 2)
        if n % 2 == 0:
            for j in range(1, n, 2):
                print(2, end=' ')
                print(j, j + 1)
        else:
            print(3, 1, 2, 3)
            j = 4
            while j < n:
                print(2, end=' ')
                print(j, j + 1)
                j = j + 2
