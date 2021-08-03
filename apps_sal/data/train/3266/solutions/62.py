def my_first_kata(a, b):
    try:
        if type(a) is bool or type(b) is bool:
            raise TypeError('why')
        return a % b + b % a
    except TypeError:
        return False
