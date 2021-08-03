def two_highest(arg1):
    x = []
    y = []
    z = []
    if len(arg1) == 0:
        return []
    elif len(arg1) == 1:
        return arg1
    else:

        x = sorted(arg1, reverse=True)
        for i in range(len(x)):
            if x[i] in y:
                y = y
            else:
                y.append(x[i])
        z.append(y[0])
        z.append(y[1])
        return z
