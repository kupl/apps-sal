def tidyNumber(n):
    return ([int(i) for i in str(n)]) == (sorted([int(i) for i in str(n)]))
