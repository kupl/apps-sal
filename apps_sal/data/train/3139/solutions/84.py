def index(array, n):
    return pow(array.pop(n), n) if len(array) > n else -1
