def tidyNumber(n):
    return str(n) == ''.join(sorted(str(n)))
    # return all(x <= y for x, y in zip(str(n), str(n)[1:]))
