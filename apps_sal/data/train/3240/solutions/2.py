def true_binary(n):
    return [1] + [1 if b=='1' else -1 for b in bin(n)[2:-1]]
