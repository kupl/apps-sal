def index(array, n):
    try:
        return array[n]**n
    except:
        return -1


print(index([1, 2, 3, 4], 2))
