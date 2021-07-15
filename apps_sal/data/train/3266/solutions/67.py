def my_first_kata(a,b):
    if type(a) != type(5) or type(b) != type(5): return False
    else:
        return a % b + b % a
