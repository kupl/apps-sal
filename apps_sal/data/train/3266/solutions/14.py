def my_first_kata(a, b):
    if type(a) == type(b) == int:
        return a % b + +b % a
    else:
        return False
