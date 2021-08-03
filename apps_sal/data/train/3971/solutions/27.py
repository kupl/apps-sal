def tidyNumber(n):

    d = [int(x) for x in str(n)]

    if all(i <= j for i, j in zip(d, d[1:])):

        return True

    else:

        return False
