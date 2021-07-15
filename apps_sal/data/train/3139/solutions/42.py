def index(array, n):

    for i, val in enumerate(array):
        if n == i:
            return  val ** n
    else:
        return -1
        

