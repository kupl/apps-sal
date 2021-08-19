def nbr_of_laps(x, y):
    print(x, y)
    if x != y:
        a = round(y * (x / y))
        b = round(x * (y / x))
        if x == a and y == b:
            for i in reversed(range(100)):
                if a % (i + 2) == 0 and b % (i + 2) == 0:
                    print(i + 2)
                    return (b / (i + 2), a / (i + 2))
            else:
                return (b, a)
    elif x == y:
        return (1, 1)
