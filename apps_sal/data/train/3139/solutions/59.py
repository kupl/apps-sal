def index(array, n):
    if n > len(array)-1:
        return -1
    else:
        number = array[n]
        return number**n
