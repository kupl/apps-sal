def my_first_kata(a,b):
    if type(a) is type(b):
        return a % b + b % a
    else:
        return False
