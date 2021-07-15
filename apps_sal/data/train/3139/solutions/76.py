def index(array, n):
    if (n > len(array) - 1):
        return -1
    else:
        result = 1
        i = 0
        while (i < n):
            result *= array[n]
            i += 1
        return result
