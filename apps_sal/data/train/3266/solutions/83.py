def my_first_kata(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return False
    elif a != 0 and b != 0:
        return a % b + b % a
    else:
        return False
