def index(array, n):
    if len(array) - 1 < n:
        a = -1
        return(a)
    else:
        return(array[n]**n)
