def two_count(n):

    binaryArr = list(bin(n))

    binaryArr.reverse()

    return binaryArr.index('1')
