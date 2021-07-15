def evil(n):
    n_bin = bin(n)[2:]
    ones = n_bin.count('1')
    if (ones % 2 != 0):
        return 'It\'s Odious!'
    else:
        return 'It\'s Evil!'
