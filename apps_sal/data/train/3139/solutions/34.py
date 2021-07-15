def index(array, n):
    if (len(array)<n+1):
        return -1
    else:
        return pow(array[n],n)
