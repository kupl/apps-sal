def my_first_kata(a, b):
    if a == None or b == None:
        return False
    if a == [] or b == []:
        return False
    try:
        if a != 0 and b != 0:
            return a % b + b % a
    except TypeError:
        return False
