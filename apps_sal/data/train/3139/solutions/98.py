def index(array=[], n=0):
    if n >= len(array):
        return -1
    else:
        return array[n] ** n
