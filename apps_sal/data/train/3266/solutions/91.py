def my_first_kata(a, b):

    if isinstance(a, bool) or isinstance(b, bool):
        return False
    if (not isinstance(a, int)) or (not isinstance(b, int)):
        return False
    elif a == 0 or b == 0:
        return False

    else:
        return a % b + + b % a
