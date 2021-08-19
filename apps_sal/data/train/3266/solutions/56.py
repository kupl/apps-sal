def my_first_kata(a, b):
    if isinstance(a, int) and isinstance(b, int) and (not isinstance(b, bool)) and (not isinstance(a, bool)):
        return a % b + b % a
    else:
        return False
