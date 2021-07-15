def index(array, n):
    if len(array) <= n :
        return -1 
    else:
        nth = array[n]
        nth_sq = nth ** n
    return nth_sq

