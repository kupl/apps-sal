def my_first_kata(a, b):
    print(a, b)
    if isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool) and not isinstance(b, bool):
        return a % b + b % a
    else:
        return False
