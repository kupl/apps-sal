def is_magical(sq):
    return all((sum(sq[i * 3:i * 3 + 3]) == sum(sq[i::3]) == 15 for i in range(3))) and sum(sq[::4]) == 15
