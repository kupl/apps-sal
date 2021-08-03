def index(array, n):
    if (len(array) - 1) >= n:
        for i in range(len(array)):
            return array[n]**n
    else:
        return -1
