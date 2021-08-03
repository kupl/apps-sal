def __starting_point():
    T = int(input())
    while T > 0:
        T = T - 1
        n = int(input())
        num = int(input())
        num = num % n
        num2 = n - num
        if num2 == num:
            print(num * 2 - 1)
        else:
            print(min(num, num2) * 2)


__starting_point()
