def index(array, n):
    try:
        return array[n]**n
    except IndexError:
        return -1
    finally:
        pass
