def get_real_floor(n):
    # code here
    if n > 13:
        return n - 2
    if n < 13 and n > 1:
        return n - 1
    if n < 0:
        return n
    else:
        return 0
