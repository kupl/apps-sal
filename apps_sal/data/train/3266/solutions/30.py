def my_first_kata(a, b):
    if type(a) == int and type(b) == int:  # both must be stated as int
        return a % b + b % a
    else:
        return False
