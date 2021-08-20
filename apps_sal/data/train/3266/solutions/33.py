def my_first_kata(a, b):
    try:
        if type(a) == str or type(b) == str:
            return False
        if type(a) == dict or type(b) == dict:
            return False
        else:
            return a % b + b % a
    except ZeroDivisionError:
        pass
