def total_inc_dec(x):
    def combination(n, m):
        if m == 0:
            return 1
        else:
            a = b = 1
            for i in range(0, m):
                a *= n - i
                b *= i + 1
            return int(a / b)

    def coefficientList(x):
        if x == 1:
            return [2]
        elif x == 2:
            return [2, 5]
        else:
            List1 = coefficientList(x - 1)
            List = [2] * x
            for i in range(0, x - 2):
                List[i + 1] = List1[i] + \
                    List1[i + 1]
            List[-1] = List1[-1] + x + 1
            return List

    if x == 0:
        return 1
    else:
        List = coefficientList(x)
        a = 0
        for i in range(0, len(List)):
            a += List[i] * combination(9, x - i)
        a = 1 + a - x * combination(9, 1)
        return a
