def get_real_floor(n):
    # code here
    if n == 0:
        return 0
    elif n > 0 and n <= 13:
        n = n - 1
        return n
    elif n > 0 and n > 13:
        n = n - 2
        return n
    elif n < 0:
        return n
