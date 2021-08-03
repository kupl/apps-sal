def calculate(expression):
    print(expression)
    expression = "".join([" {} ".format(num) if num in "+-*$" else num for num in expression]).split()
    while '$' in expression:
        try:
            for num in expression:
                if num == '$':
                    first = expression.pop(expression.index(num) - 1)
                    second = expression.pop(expression.index(num) + 1)
                    ans = str(float(float(first) / float(second)))
                    expression[expression.index(num)] = ans
        except ValueError:
            return '400: Bad request'
    while '*' in expression:
        try:
            for num in expression:
                if num == '*':
                    first = expression.pop(expression.index(num) - 1)
                    second = expression.pop(expression.index(num) + 1)
                    ans = str(float(float(first) * float(second)))
                    expression[expression.index(num)] = ans
        except ValueError:
            return '400: Bad request'
    while '-' in expression:
        try:
            for num in expression:
                if num == '-':
                    first = expression.pop(expression.index(num) - 1)
                    second = expression.pop(expression.index(num) + 1)
                    ans = str(float(float(first) - float(second)))
                    expression[expression.index(num)] = ans
        except ValueError:
            return '400: Bad request'
    while '+' in expression:
        try:
            for num in expression:
                if num == '+':
                    first = expression.pop(expression.index(num) - 1)
                    second = expression.pop(expression.index(num) + 1)
                    ans = str(float(float(first) + float(second)))
                    expression[expression.index(num)] = ans
        except ValueError:
            return '400: Bad request'
    try:
        return float(expression[0])
    except ValueError:
        return '400: Bad request'
