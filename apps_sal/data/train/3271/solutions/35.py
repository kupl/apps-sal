def arr(n = None): 
    array = []
    if n is None:
        return array
    elif n >= 0:
        for i in range(n):
            array.append(i)
        return array
