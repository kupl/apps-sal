def is_magical(sq):
    return all((sum(sq[i * 3:(i + 1) * 3]) == sum(sq[i:9:3]) for i in range(0, 3)))
