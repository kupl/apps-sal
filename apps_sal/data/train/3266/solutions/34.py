def my_first_kata(a, b):
    try:
        return a % b + b % a if all(map(lambda x: type(x) == int, (a, b))) else False
    except ZeroDivisionError:
        return False
