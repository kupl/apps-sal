def calculate(num1, operation, num2):
    # your code here
    try:
        return eval("{} {} {}".format(num1, operation, num2))
    except (ZeroDivisionError, SyntaxError):
        return None
