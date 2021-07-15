def my_first_kata(a,b):
    if isinstance(a, bool) or isinstance(b, bool):
        return False
    if isinstance(a, int) and isinstance(b, int) and a != 0 and b != 0: 
        return a % b + b % a
    else:
        return False
