def tidyNumber(n):
    return n == int(''.join(sorted((i for i in str(n)))))
