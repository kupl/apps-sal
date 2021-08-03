def sum_of_n(n):
    if n < 0:
        minus = True
    else:
        minus = False
    return [-sum(range(k + 1)) if minus else sum(range(k + 1)) for k in range(abs(n) + 1)]
