def stringy(size):
    if size % 2 == 0:
        return int(size / 2) * '10'
    else:
        return int(size / 2) * '10' + '1'


# the string should start with a 1.

# a string with size 6 should return :'101010'.

# with size 4 should return : '1010'.

# with size 12 should return : '101010101010'.
