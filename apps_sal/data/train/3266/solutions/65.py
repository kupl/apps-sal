def my_first_kata(a, b):
    print(a, b)
    if not all((isinstance(x, int) for x in [a, b])):
        return False
    elif int(a) == 0 or int(b) == 0:
        return False
    else:
        return a % b + b % a
