def index(array, n):
    if len(array) - 1 < n:
        return - 1
    for ind, value in enumerate(array):
        if ind == n:
            return(value**n)
