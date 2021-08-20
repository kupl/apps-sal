def true_binary(n):
    return [1] + [int(c) * 2 - 1 for c in bin(n)[2:-1]]
