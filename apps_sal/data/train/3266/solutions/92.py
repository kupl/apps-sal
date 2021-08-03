def my_first_kata(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return False
    else:
        try:
            return a % b + b % a
        except ZeroDivisionError:
            return False
