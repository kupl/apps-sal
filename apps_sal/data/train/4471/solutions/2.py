def lamps(a):
    case1c = 0
    case2c = 0
    for i in range(len(a)):
        if i % 2 == 0:
            if a[i] == 1:
                case1c += 1
            else:
                case2c += 1
        else:
            if a[i] == 1:
                case2c += 1
            else:
                case1c += 1
    return min(case1c, case2c)
