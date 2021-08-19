def stringy(size):
    if size % 2 == 0:
        return int(size / 2) * '10'
    else:
        return int(size / 2) * '10' + '1'
