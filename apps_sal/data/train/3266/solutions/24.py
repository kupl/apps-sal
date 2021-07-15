def my_first_kata(a,b):
    if type(a) != int or type(b) != int:
        return False
    elif a == 0 or b == 0:
        return False
    else:
        return a % b + b % a
