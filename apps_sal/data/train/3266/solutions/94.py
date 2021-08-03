def my_first_kata(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return False
    else:
        if a * b == 0:
            return False
        return a % b + b % a
