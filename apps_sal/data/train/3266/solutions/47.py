def my_first_kata(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a % b + b % a
    else:
        return False
