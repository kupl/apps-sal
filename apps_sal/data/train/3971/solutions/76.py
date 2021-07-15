def tidyNumber(n):
    return n == int(''.join(sorted([x for x in str(n)])))
