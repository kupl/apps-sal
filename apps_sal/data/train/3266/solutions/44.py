def my_first_kata(a, b):
    numbers = [int, float, complex]
    if type(a) in numbers and type(b) in numbers:
        return a % b + b % a
    return False
