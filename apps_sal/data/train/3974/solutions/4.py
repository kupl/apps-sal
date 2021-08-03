def two_count(n):

    # store the brinary digits of n as an array
    binaryArr = list(bin(n))

    # reverse the array
    binaryArr.reverse()

    # return the index of the first location of element '1'
    return binaryArr.index('1')
