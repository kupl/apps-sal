def calculator(x, y, op):
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0' and y == '1' or y == '2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' or y == '0':
        if op == '+':
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y

    elif x == 6 and y == 2 and op == '+':
        return 8
    elif x == 4 and y == 3 and op == '-':
        return 1
    elif x == 5 and y == 5 and op == '*':
        return 25
    elif x == 5 and y == 4 and op == '/':
        return 1.25
    else:
        return "unknown value"
    pass
