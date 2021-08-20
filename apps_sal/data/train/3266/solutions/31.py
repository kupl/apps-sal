def my_first_kata(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return False
    try:
        sum = a % b + b % a
        return sum
    except ZeroDivisionError:
        return False
