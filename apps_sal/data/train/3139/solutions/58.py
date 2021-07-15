def index(array, n):
    if n < len(array):
        a = array[n]
        num = a ** n
        return num
    else:
        return -1

