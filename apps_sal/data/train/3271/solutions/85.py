def arr(n=None):
    # [ the numbers 0 to N-1 ]
    array = []
    if(n is not None and n >= 0):
        for i in range(n):
            array.append(i)
    return array
