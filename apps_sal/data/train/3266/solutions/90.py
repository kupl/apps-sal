def my_first_kata(a, b):
    if type(a) != type(1) or type(b) != type(1):
        return False
    elif type(a) == type(1) or type(b) == type(1):
        return a % b + b % a
