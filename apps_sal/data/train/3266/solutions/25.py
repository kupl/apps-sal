def my_first_kata(a, b):
    if isinstance(a, int) and isinstance(b, int) and a * b != 0:
        return a % b + b % a
    else:
        return False
