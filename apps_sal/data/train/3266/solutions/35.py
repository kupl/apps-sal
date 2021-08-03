def my_first_kata(a, b):
    if 'int' in str(type(a)) and 'int' in str(type(b)):
        return a % b + b % a
    else:
        return False
