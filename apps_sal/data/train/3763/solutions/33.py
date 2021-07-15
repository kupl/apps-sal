def calculator(x, y, op):
    if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
        while True:
            try:
                if op == '*':
                    sumMUL = float(x * y)
                    print(sumMUL)
                    return sumMUL

                if op == '+':
                    sumADD = float(x + y)
                    return sumADD
                    print(sumADD)
                if op == '-':
                    sumSUB = float(x - y)
                    return sumSUB
                elif op == '/':
                    sumDIV = float(x / y)
                    return sumDIV
                else:
                    return "unknown value"
                break
            except TypeError:
                return "unknown value"
    else:
        return "unknown value"
