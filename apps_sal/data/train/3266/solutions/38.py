def my_first_kata(a, b):
    if type(a) != float and type(a) != int or (type(b) != float and type(b) != int):
        return False
    else:
        return a % b + b % a
