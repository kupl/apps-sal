def points(dice):
    x = sorted(dice)
    if len(set(x)) == 1:
        return 50

    if len(set(x)) == 2:
        for i in set(x):
            if dice.count(i) in [1, 4]:
                return 40
            else:
                return 30

    if x[0] == '1':
        exp = [x[0], x[1]]
        for i in range(1, 4):
            n = int(x[1]) + i
            if n > 6:
                exp.append(str(n % 6))
            else:
                exp.append(str(n))
        if exp == x:
            return 20
    else:
        exp = [x[0]]
        for i in range(1, 5):
            n = int(x[0]) + i
            if n > 6:
                exp.append(str(n % 6))
            else:
                exp.append(str(n))
        if exp == x:
            return 20
        else:
            return 0
    return 0
