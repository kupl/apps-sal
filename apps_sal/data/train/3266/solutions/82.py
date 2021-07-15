def my_first_kata(a,b):
    if a == 0 or b == 0:
        return False
    elif isinstance(a, int) and isinstance(b, int):
        a = int(a)
        b = int(b)
        return a % b ++ b % a
    else:
        return False
