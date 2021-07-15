def index(array, n):
    if n >= 0 and n < len(array):
        x = 1
        for i in range(n):
            x = x * array[n]
        return x
    else:
        return -1

