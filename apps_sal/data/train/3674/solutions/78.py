def add_binary(a,b):
    return str(bin(a+b))[2:]
    #seems to be faster than "{0:b}".format(a+b)

