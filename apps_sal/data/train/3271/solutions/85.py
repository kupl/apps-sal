def arr(n=None):
    array = []
    if(n is not None and n >= 0):
        for i in range(n):
            array.append(i)
    return array
