def consecutive_ducks(n):
    return (((n & (n - 1)) != 0) and n != 0)
