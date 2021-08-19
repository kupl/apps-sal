def is_magical(sq):
    return len(set([sum(sq[i * 3:(i + 1) * 3]) for i in range(3)]                # lines
                   + [sum(sq[i::3]) for i in range(3)]                # rows
                   + [sq[4 - 2 * i] + sq[4] + sq[4 + 2 * i] for i in range(1, 3)]     # diagonals
                   )) == 1
