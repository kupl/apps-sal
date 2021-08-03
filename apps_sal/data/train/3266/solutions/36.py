def my_first_kata(a, b):
    print(a, b)
    if not isinstance(a, int) and not isinstance(b, int):
        return False
    else:
        try:
            return a % b + b % a
        except:
            return False
