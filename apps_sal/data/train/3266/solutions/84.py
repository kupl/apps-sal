def my_first_kata(a,b):
    if not isinstance(a, int) or not isinstance(b, int): return False
    if a is 0 or b is 0:
        return False
    else:
        return a % b ++ b % a
