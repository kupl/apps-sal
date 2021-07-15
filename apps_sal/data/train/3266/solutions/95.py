def my_first_kata(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    else:
        return a % b + b % a
