def my_first_kata(a, b):
    if bool(type(a) == int and type(b) == int):
        return (a % b + b % a)
    else:
        return False
