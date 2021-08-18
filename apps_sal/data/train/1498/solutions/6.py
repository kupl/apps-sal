try:
    from functools import reduce

    def factors(n):
        return set(reduce(list.__add__,
                          ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    b = ()
    test = int(input())
    for i in range(test):
        flag = 0
        move = 1000
        h, x, y = list(map(int, input().split(' ')))
        b = factors(h - 1)
        h -= 1
        if(h == x):
            print("0")
            move = 999
        else:
            for j in b:
                if(j >= x):
                    if(j == x):
                        flag = 1
                        if(move > h // j):
                            move = h // j
                    elif((j - x) % y == 0):
                        flag = 1
                        if(move > ((j - x) // y + h / j)):
                            move = ((j - x) // y + h / j)

            if(flag == 0):
                print("-1")
            else:
                print(int(move) % ((10**9) + 7))


except EOFError:
    pass
