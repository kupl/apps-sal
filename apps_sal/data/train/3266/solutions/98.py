def my_first_kata(a,b):
    if a == 0 or b == 0:
        return False
    if isinstance(a, int) and isinstance(b, int): 
        return a%b + b%a
    else:
        return False
