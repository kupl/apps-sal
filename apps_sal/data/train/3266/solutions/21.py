def my_first_kata(a,b):
    print(a)
    print(b)
    valid_a = isinstance(a, int) and type(a) == type(0)
    valid_b = isinstance(b, int) and type(b) == type(0)
    if valid_a and valid_b:
        return a % b + b % a
    else:
        return False
