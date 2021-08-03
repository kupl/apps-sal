def my_first_kata(a, b):
    if not type(a) in (int, float) or not type(b) in (int, float):
        return False
    return a % b + b % a
