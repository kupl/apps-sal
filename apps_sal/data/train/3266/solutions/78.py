def my_first_kata(a,b):
    if type(a) == int:
        if type(b) == int: 
            return a % b + b % a 
    return False
