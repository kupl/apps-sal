def tidyNumber(n):
    return True if sorted([int(x) for x in str(n)]) == [int(x) for x in str(n)] else False
