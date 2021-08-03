def my_first_kata(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return False
    if a == 0 or b == 0:
        return False
    return a % b + b % a
