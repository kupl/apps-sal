def square(n,y=2):
    if y == 1:
        return n
    else:
        return n * square(n, y - 1)

