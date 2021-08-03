def my_first_kata(a, b):
    if type(a) == type(b) == int:
        try:
            return a % b + b % a
        except ZeroDivisionError:
            return False
    else:
        return False
