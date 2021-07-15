def code(x,y):
    return sum(int(str(n).translate(str.maketrans('0123456789','9876543210'))) for n in [x,y])
