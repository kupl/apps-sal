def my_first_kata(a, b):
    if type(a) in (int, float) and type(b) in (int, float):
        return a % b + b % a
    return False
