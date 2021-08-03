def angle(n):
    if n < 3:
        print('Has to be a shape, try again')
    elif n == 3:
        return 180
    elif n > 3:
        n = ((n - 4) * 180 + 360)
    return n
