def is_even(n):
    try:
        return bin(n)[-1] == '0'
    except TypeError:
        return False
