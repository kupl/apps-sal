def tidyNumber(n):
    return n == int(''.join(x for x in sorted(list(str(n)))))
