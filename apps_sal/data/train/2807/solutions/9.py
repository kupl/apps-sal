def consecutive_ducks(n):
    while n > 1:
        n = n / 2
        if str(n).split('.')[1] != '0':
            return True
    return False
