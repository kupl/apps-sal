def my_first_kata(a, b):
    x = isinstance(a, int)
    y = isinstance(b, int)
    if x and y == True:
        if a and b > 0:
            return a % b + b % a
        else:
            return False
    else:
        return False
