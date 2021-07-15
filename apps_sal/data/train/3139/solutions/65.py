def index(array, n):
    while True:
        try:
            return array[n] ** n 
            break
        except IndexError:
            return -1
