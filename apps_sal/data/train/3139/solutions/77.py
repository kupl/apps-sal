def index(array, n):
    if n > len(array) - 1:
        return(-1)
    elif n == 0:
        return(1)
    else:
        pw = array[n]
        i = 1
        while i != n:
            array[n] *= pw
            i += 1
        return(array[n])
