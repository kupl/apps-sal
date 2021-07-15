def index(array, n):
    try:
        return array[n] ** n
    except (IndexError, TypeError):
        return -1
