def calculate(num1, operation, num2):
    try:
        return eval("{} {} {}".format(num1, operation, num2))
    except (ZeroDivisionError, SyntaxError):
        return None
