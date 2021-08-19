def stringy(size):
    binary_yo = ''
    for i in range(size):
        if i % 2 == 0:
            binary_yo += '1'
        else:
            binary_yo += '0'
    return binary_yo
