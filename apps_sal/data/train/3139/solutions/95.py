def index(array, n):
    if((len(array)) - 1) < n:
        return(-1)
    else:
        for i in range(len(array)):
            print((n, i))
            if (n == i):
                return(array[i]**n)
