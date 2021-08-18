try:
    T = int(input())
    while T > 0:
        n = int(input())
        i = 1
        for j in range(n // 2 - 1):
            print(i + 1, i, end=" ")
            i += 2
        if n % 2 == 0:
            print(i + 1, i)
        else:
            print(i + 1, i + 2, i)
        T -= 1
except:
    pass
