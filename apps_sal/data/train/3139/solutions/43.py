def index(array, n):
    result = 1
    if n > len(array) - 1:
        return -1
    else:
        for index in range(n):
            result = result * array[n]
    return result
