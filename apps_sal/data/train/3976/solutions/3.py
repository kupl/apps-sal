def last(*arr):
    return arr[-1] if type(arr[-1]) == int else arr[-1][-1]
