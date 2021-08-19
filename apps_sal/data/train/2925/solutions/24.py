def multiply(n):
    n_multiply = len(str(n).strip('-'))
    for i in range(n_multiply):
        n = n * 5
    return n
