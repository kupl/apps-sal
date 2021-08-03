def my_first_kata(a, b):
    return False if isinstance(a, (str, bool, dict)) or isinstance(b, (str, bool, dict)) else a % b + b % a
