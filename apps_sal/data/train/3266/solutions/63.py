def my_first_kata(a, b):
    for item in (a, b):
        if type(item) != int:
            return False
    return a % b + + b % a
