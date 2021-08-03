def my_first_kata(a, b):
    return a % b + b % a if (isinstance(a, int) and isinstance(b, int) and a and b) else False
