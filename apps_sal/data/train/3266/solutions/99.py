def my_first_kata(a, b):
    return False if not isinstance(a, int) or not isinstance(b, int)\
        or a == 0 or b == 0 else a % b + b % a
