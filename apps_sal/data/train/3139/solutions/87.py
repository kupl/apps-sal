def index(array, n):
    if n > -1 and n < len(array):
        product = array[n]**n
    else:
        product = -1

    return product
