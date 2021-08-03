def index(array, n):
    if n >= len(array):  # Here, the nth index will be outside the array.
        return -1
    else:
        return array[n] ** n
