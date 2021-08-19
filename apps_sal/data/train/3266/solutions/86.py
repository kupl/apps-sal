def my_first_kata(a, b):
    if isinstance(a, int) == False or isinstance(b, int) == False:
        return False
    else:
        return a % b + +b % a
