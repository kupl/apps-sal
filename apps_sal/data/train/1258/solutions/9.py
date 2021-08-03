for _ in range(int(input())):
    a = input()
    res = sum(map(int, a))
    if len(a) > 1 and res < 9:
        print(9 - res)
    else:
        print(min(9 - res % 9, res % 9))
