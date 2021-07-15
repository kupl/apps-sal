def get_real_floor(n):
    return n - (n>0 and 1) - (n>13 and 1)
