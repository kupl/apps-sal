def true_binary(n):
    return [-1 if x == '0' else 1 for x in bin(n)[1:-1]]
